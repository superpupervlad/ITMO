#include "Client.h"

void Client::connect_to_server(const char * ip, unsigned port_){
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

void Client::send_msg(const char * msg){
    write(fd, msg, strlen(msg));
}

void Client::send_code(char code){
    write(fd, &code, 1);
}

void Client::send_args(int arg_num, ...){
    va_list valist;
    va_start(valist, arg_num);

    char res[1024];
    strcpy(res, va_arg(valist, char *));
    strcat(res, "!");
    for (int i = 1; i < arg_num; i++) {
        strcat(res, va_arg(valist, char *));
        strcat(res, "!");
    }

    va_end(valist);

    send_msg(res);
}

void Client::send_args(std::vector<std::string> strings){
    std::string res;
    for (int i = 0; i < strings.size(); i++){
        res.append(strings[i]);
        res.append("!");
    }
    send_msg(res);
}

void Client::send_msg(std::string msg){
    write(fd, msg.c_str(), strlen(msg.c_str()));
}

char * Client::safe_send_code(char code){
    send_code(code);
    printf("1");
    return aftersend(code);
}

char * Client::aftersend(char code){
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

char * Client::recieve_msg(){
    char * buf = (char *)malloc(1024 * sizeof(char));
    ssize_t nread = 0;
    while (nread == 0)
        nread = read(fd, buf, 1024);
    return buf;
}

char Client::recieve_code(){
    char code;
    ssize_t nread = 0;
    while (nread == 0)
        nread = read(fd, &code, 1);
    return code;
}

std::vector<std::string> Client::parse_args(char * args){
    return split((std::string)args);
}

void Client::quit(){
    close(fd);
}

char * Client::launch_proc(const char * name, const char * parameters, const char * uid){
    send_code(LAUNCH_PROC);
    send_args(3, name, parameters, uid);
    return recieve_msg();
}

int Client::launch_proc_bg(const char * name, const char * parameters, const char * uid){
    send_code(LAUNCH_PROC_BG);
    send_args(3, name, parameters, uid);
    return atoi(recieve_msg());
}

// 4.5.9
bool Client::log(){
    std::vector<std::string> data;
    data.push_back(login);
    data.push_back(pass);
    send_args(data);
    return recieve_code();
}

char * Client::get_proc_info(int pid){
    send_code(GET_PROC_INFO);
    send_msg(std::to_string(pid));
    return recieve_msg();
}