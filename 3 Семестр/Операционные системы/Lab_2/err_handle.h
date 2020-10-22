#ifndef LAB_2_1_ERR_HANDLE_H
#define LAB_2_1_ERR_HANDLE_H

#include <sys/types.h>
#include <sys/socket.h>

short Socket (int domain, int type, int protocol);

void Bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen);

void Listen(int sockfd, int backlog);

short Accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);

void Inet_pton(int af, const char *src, void *dst);

void Connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen);

void sig_handler(int num);

#endif //LAB_2_1_ERR_HANDLE_H
