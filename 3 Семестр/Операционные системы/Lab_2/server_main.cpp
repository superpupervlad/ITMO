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

int main() {
    signal(SIGINT, sig_int_handler);
    signal(SIGTERM, sig_term_handler);

    Server s{};
    s.wait_connection();
    while(!s.check_login()) {}

    s.handle_code(s.recieve_code());
    s.handle_code(s.recieve_code());

    s.shutdown();
}

