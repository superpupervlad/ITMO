#include <iostream>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#include "err_handle.h"
#include "codes.h"

#define PORT 12341
#define SERVER_IP "127.0.0.1"

class Client{
public:
    unsigned port;
    const char * server_ip;
    short fd;

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

    char * safe_send_code(char code){
        send_code(code);
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
            case GET_TIME:
                return recieve_msg();
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
        //printf("d:'%d', c:'%c'", code, code);
        return code;
    }

    void quit(){
        close(fd);
    }
};

int main(){
    //printf("0");
    Client c{};
    c.connect_to_server(SERVER_IP, PORT);
    printf("-%s-", c.safe_send_code(PING));

    c.quit();
}
