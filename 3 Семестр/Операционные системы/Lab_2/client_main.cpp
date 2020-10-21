#include <iostream>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdarg.h>


#include "err_handle.h"
#include "codes.h"
#include "unilib.h"

#define PORT 12347
#define SERVER_IP "127.0.0.1"

class Client{
public:
    unsigned port;
    const char * server_ip;
    short fd;
    std::string login = "primi";
    std::string pass = "labu";

    void connect_to_server(const char * ip, unsigned port_){
        port = port_;
        server_ip = ip;

        fd = Socket(AF_INET, SOCK_STREAM, 0);

        struct sockaddr_in addr = {0};
        addr.sin_family = AF_INET;
        addr.sin_port = htons(PORT);
        socklen_t addr_len = sizeof addr;

        Inet_pton(AF_INET, SERVER_IP, &addr.sin_addr);

        Connect(fd, (const struct sockaddr *) &addr, addr_len);
    }

    void send_msg(const char * msg){
        write(fd, msg, strlen(msg));
    }

    void send_code(char code){
        write(fd, &code, 1);
    }

    void send_args(int arg_num, ...){
        va_list valist;
        va_start(valist, arg_num);

        char res[256];
        strcpy(res, va_arg(valist, char *));
        strcat(res, "!");
        for (int i = 1; i < arg_num; i++) {
            strcat(res, va_arg(valist, char *));
            strcat(res, "!");
        }

        va_end(valist);

        send_msg(res);
    }

    void send_args(std::vector<std::string> strings){
        std::string res;
        for (int i = 0; i < strings.size(); i++){
            res.append(strings[i]);
            res.append("!");
        }
        send_msg(res);
    }

    void send_msg(std::string msg){
        write(fd, msg.c_str(), strlen(msg.c_str()));
    }

    char * safe_send_code(char code){
        send_code(code);
        printf("1");
        return aftersend(code);
    }

    char * aftersend(char code){
        char * default_response = (char *)"1"; //в рот ебал эти чары и звездочки СУКА
        //char *c = (char *)malloc(sizeof(char));

        switch (code) {
            case PING:
                if (recieve_code() == PING)
                    return default_response;
//                *c = recieve_code();
//                return c;
            case GET_DATETIME:
                return recieve_msg();
//            case LAUNCH_PROC:
//                return launch_proc();
            default:
                return default_response;
        }
    }

    char * recieve_msg(){
        char * buf = (char *)malloc(256 * sizeof(char));
        ssize_t nread = 0;
        while (nread == 0)
            nread = read(fd, buf, 256);
        return buf;
    }

    char recieve_code(){
        char code;
        ssize_t nread = 0;
        while (nread == 0)
            nread = read(fd, &code, 1);
        return code;
    }

    void quit(){
        close(fd);
    }

    char * launch_proc(const char * name, const char * parameters, const char * uid){
        send_code(LAUNCH_PROC);
        send_args(3, name, parameters, uid);
        return recieve_msg();
    }

    // 4.5.9
    bool log(){
        std::vector<std::string> data;
        data.push_back(login);
        data.push_back(pass);
        send_args(data);
        return recieve_code();
    }
};

int main(){
    Client c{};
    c.connect_to_server(SERVER_IP, PORT);
    c.log();

    printf("%s", c.launch_proc("ls -lah", " ", " "));

    c.quit();
}
