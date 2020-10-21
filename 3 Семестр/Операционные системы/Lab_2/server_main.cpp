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

class Server{
public:
    unsigned port = PORT;
    short fd;
    short sock;

    bool wait_connection(){
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

    void handle_code(char msg){
        switch (msg) {
            case PING:
                send_code(PING); break;
            case GET_TIME:
                send_msg("21:35"); break;
            default:
                return;
        }
    }

    void send_msg(const char * msg){
        write(fd, msg, strlen(msg));
    }

    void send_code(char code){
//        printf(".%c.", code);
//        std::cout << "-" << code << "-";
        write(fd, &code, 1);
    }

    char * recieve_msg(){
        char * buf = (char *)malloc(256 * sizeof(char));
        ssize_t nread = 0;
        while (nread == 0)
             nread = read (fd, buf, 256);
        return buf;
    }

    char recieve_code(){
        char code;
        ssize_t nread = 0;
        while (nread == 0)
            nread = read(fd, &code, 1);
        return code;
    }

    void shutdown(){
        sleep(1);
        close(fd);
        close(sock);
    }
};

int main() {
    Server s{};
    s.wait_connection();
    s.handle_code(s.recieve_code());
    s.shutdown();
}

