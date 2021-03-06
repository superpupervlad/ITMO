#include <iostream>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdarg.h>
#include <vector>
#include <signal.h>
#include <filesystem>
#include <algorithm>

#include "err_handle.h"
#include "codes.h"
#include "server_processes.h"
#include "unilib.h"
#include "Server.h"

Server * global_serv;

namespace fs = std::filesystem;

void sig_int_handler(int num){
    global_serv->shutdown();
    write(STDOUT_FILENO, "Goodbye\n", 9);
}

void sig_term_handler(int num){
    global_serv->shutdown();
    write(STDOUT_FILENO, "Goodbye\n", 9);
}

Server::Server() {
    global_serv = this;
}

bool Server::wait_connection(){
    sock = Socket(AF_INET, SOCK_STREAM, 0); //descriptor
    //printf("%d", sock);

    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    socklen_t addr_len = sizeof(addr);
    Bind(sock, (struct sockaddr *) &addr, addr_len);

    Listen(sock, 1);

    fd = Accept(sock, (struct sockaddr *) &addr, &addr_len);

    connected = true;

    return true;
}

void Server::handle_code(char msg){
    switch (msg) {
        case PING:
            send_code(PING); break;
        case GET_DATETIME:
            send_msg(get_time()); break;
        case LAUNCH_PROC:{
            std::vector<std::string> a = parse_args(recieve_msg());
            send_msg(launch_proc(
                    (const char *) a[0].c_str(),
                    (const char *) a[1].c_str(),
                    1));
            break;
        }
        case LAUNCH_PROC_BG:{
            std::vector<std::string> a = parse_args(recieve_msg());
            send_msg(std::to_string(launch_proc_bg(
                    (const char *) a[0].c_str(),
                    (const char *) a[1].c_str(),
                    1)));
            break;
        }
        case GET_PROC_INFO:{
            int pid = atoi(recieve_msg());
            Process p = get_proc_info(pid);
            send_proc_info(p);
        }
        default:
            return;
    }
}

void Server::send_msg(const char * msg){
    write(fd, msg, strlen(msg));
}

void Server::send_msg(std::string msg){
    write(fd, msg.c_str(), strlen(msg.c_str()));
}

void Server::send_code(char code){
//        printf(".%c.", code);
//        std::cout << "-" << code << "-";
    write(fd, &code, 1);
}

void Server::send_file(FILE * f){
    // maybe not working
    char c = fgetc(f);
    while (c != EOF){
        write(fd, &c, 1);
        c = fgetc(f);
    }
}

void Server::send_args(int arg_num, ...){
    va_list valist;
    va_start(valist, arg_num);

    char res[1024];
    strcpy(res, va_arg(valist, char *));
    strcpy(res, "!");
    for (int i = 1; i < arg_num; i++) {
        strcat(res, va_arg(valist, char *));
        strcat(res, "!");
    }

    va_end(valist);

    send_msg(res);
}

char * Server::recieve_msg(){
    char * buf = (char *)malloc(1024 * sizeof(char));
    ssize_t nread = 0;
    while (nread == 0)
        nread = read (fd, buf, 1024);
    return buf;
}

char Server::recieve_code(){
    char code;
    ssize_t nread = 0;
    while (nread == 0)
        nread = read(fd, &code, 1);
    return code;
}

void Server::shutdown(){
    if (connected) {
        close(fd);
        close(sock);
        exit(0);
    }
    exit(0);
}

std::vector<std::string> Server::parse_args(char * args){
    return split((std::string)args);
}

// 4.5.9
bool Server::check_login(){
    std::vector<std::string> auth = parse_args(recieve_msg());
    if (auth[0] == login and auth[1] == pass) {
        send_code(GOOD);
        return true;
    }
    else {
        send_code(BAD);
        return false;
    }
}

// 4.5.1.1
//TODO Сделать что-то с uid
int Server::launch_proc_bg(const char * name, const char * parameters, int uid){
    char result[256];
    strcpy(result, name);
    strcat(result, " ");
    strcat(result, parameters);

    pid_t pid;
    if ((pid = fork()) == 0){
        pid_t pid2;

        if ((pid2 = fork()) == 0){
            system(result);
        }
        else{
            processes.push_back(pid2);
            std::string path = "/proc";
            path.append(std::to_string(pid2));
            bool check = false;
            while (true){
                for (const auto & entry : fs::directory_iterator("/proc"))
                    if (entry.path() == path){
                        processes.erase(
                                std::find(processes.begin(), processes.end(), pid2));
                        // logger it
                        check = true;
                        break;
                    }
                if (check)
                    break;
            }
        }
    }
    else {
        return pid;
    }
}

// 4.5.1.2 return output
std::string Server::launch_proc(const char * name, const char * parameters, int uid){
    char cmd[256];
    strcpy(cmd, name);
    strcat(cmd, " ");
    strcat(cmd, parameters);

    return GetStdoutFromCommand(cmd);
}

// 4.5.2
Process Server::get_proc_info(int pid){
    Process p;
    p.pid = pid;

    int unused;
    char filename[64];
    sprintf(filename, "/proc/%d/stat", pid);
    FILE *f = fopen(filename, "r");

    fscanf(f, "%d %s %c %d", &unused, p.command, &p.state, &p.ppid);
    fclose(f);
    return p;
}

void Server::send_proc_info(Process p){
    std::string info;
    info.append("PID: " + std::to_string(p.pid) + '\n');
    info.append("PPID: " + std::to_string(p.ppid) + '\n');
    info.append("STATE: ");
    info.push_back(p.state);
    info.append("\nCOMMAND: ");
    info += p.command;
    send_msg(info);
}