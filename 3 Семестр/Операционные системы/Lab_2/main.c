#include <sys/socket.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#include "errhandle.h"
#include "lib.h"
#include "s_proc.h"

#define PORT 12345

int main(){
    int serv_socket = Socket(AF_INET, SOCK_STREAM, 0); //descriptor
    //printf("%d", serv_socket);

    get_sys_info();
    int a;
    /* struct sockaddr_in addr = {0}; */
    /* addr.sin_family = AF_INET; */
    /* addr.sin_port = htons(PORT); */
    /* socklen_t addr_len = sizeof(addr); */
    /* Bind(serv_socket, (struct sockaddr *) &addr, addr_len); */

    /* Listen(serv_socket, 1); */

    /* int fd = Accept(serv_socket, (struct sockaddr *) &addr, &addr_len); */
    /* //printf("%d", fd); */

    /* char buf[256]; */
    /* ssize_t nread = read (fd, buf, 256); */
    /* write(STDOUT_FILENO, buf, nread); */

    /* close(fd); */
    /* close(serv_socket); */
    //const char * const msg = "HELLO";
    //write(STDOUT_FILENO, msg, strlen(msg));
    return 0;
}
