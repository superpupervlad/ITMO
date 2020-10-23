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
#include "Client.h"

using std::cout;

int main(){
    Client c{};
    c.connect_to_server(SERVER_IP, PORT);
    c.log();

    //printf("%s\n", c.launch_proc("ls -lah", " ", " "));
    //printf("%d\n", c.launch_proc_bg("sleep 100", " ", " "));
    //printf("%s\n", c.get_proc_info(1));

    c.quit();
}
