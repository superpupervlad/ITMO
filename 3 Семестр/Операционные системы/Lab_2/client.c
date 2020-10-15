#include <sys/socket.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#include "errhandle.h"
#include "c_lib.h"

#define PORT 12345
#define SERVER_IP "127.0.0.1"

int main(){
    int client_socket = Socket(AF_INET, SOCK_STREAM, 0);

    /* get_l(); */
    /* struct sockaddr_in addr = {0}; */
    /* addr.sin_family = AF_INET; */
    /* addr.sin_port = htons(PORT); */
    /* socklen_t addr_len = sizeof addr; */

    /* Inet_pton(AF_INET, SERVER_IP, &addr.sin_addr); */

    /* Connect(client_socket, (const struct sockaddr *) &addr, addr_len); */

    /* write(client_socket, "Hello", 5); */

    /* close(client_socket); */
}
