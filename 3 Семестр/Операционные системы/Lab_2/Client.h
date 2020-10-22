#ifndef LAB_2_1_CLIENT_H
#define LAB_2_1_CLIENT_H

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

#define PORT 12345
#define SERVER_IP "127.0.0.1"

class Client{
public:
    unsigned port;
    const char * server_ip;
    short fd;
    std::string login = "primi";
    std::string pass = "labu";

    void connect_to_server(const char * ip, unsigned port_);

    void send_msg(const char * msg);

    void send_code(char code);

    void send_args(int arg_num, ...);

    void send_args(std::vector<std::string> strings);

    void send_msg(std::string msg);

    char * safe_send_code(char code);

    char * aftersend(char code);

    char * recieve_msg();

    char recieve_code();

    std::vector<std::string> parse_args(char * args);

    void quit();

    char * launch_proc(const char * name, const char * parameters, const char * uid);

    int launch_proc_bg(const char * name, const char * parameters, const char * uid);

    // 4.5.9
    bool log();

    char * get_proc_info(int pid);
};

#endif //LAB_2_1_CLIENT_H
