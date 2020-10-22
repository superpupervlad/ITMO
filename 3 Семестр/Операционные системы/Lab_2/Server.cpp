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

#include "err_handle.h"
#include "codes.h"
#include "server_processes.h"
#include "unilib.h"
#include "Server.h"

Server * global_serv;

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

    return true;
}

void Server::handle_code(char msg){
    switch (msg) {
        case PING:
            send_code(PING); break;
        case GET_DATETIME:
            send_msg(get_time()); break;
        case LAUNCH_PROC:{
            printf("1");
            std::vector<std::string> a = parse_args(recieve_msg());
            send_msg(launch_proc(
                    (const char *) a[0].c_str(),
                    (const char *) a[1].c_str(),
                    1));
            break;
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

    char res[256];
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
    char * buf = (char *)malloc(256 * sizeof(char));
    ssize_t nread = 0;
    while (nread == 0)
        nread = read (fd, buf, 256);
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
    sleep(1);
    close(fd);
    close(sock);
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