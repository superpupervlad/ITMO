#ifndef LAB_2_1_SERVER_H
#define LAB_2_1_SERVER_H

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

#define PORT 12347

class Server;



class Server {
public:
    bool connected = false;
    unsigned port = PORT;
    short fd;
    short sock;
    std::string login = "primi";
    std::string pass = "labu";
    std::vector<int> processes;

    Server();

    // TODO: Сделать описание методов
    bool wait_connection();
    void handle_code(char msg);
    void send_msg(const char * msg);
    void send_msg(std::string msg);
    void send_code(char code);
    void send_file(FILE * f);
    void send_args(int arg_num, ...);
    char * recieve_msg();
    char recieve_code();
    void shutdown();
    std::vector<std::string> parse_args(char * args);
    bool check_login();
    int launch_proc_bg(const char * name, const char * parameters, int uid);
};



#endif //LAB_2_1_SERVER_H
