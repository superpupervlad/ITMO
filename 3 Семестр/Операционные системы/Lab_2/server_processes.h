#ifndef LAB_2_1_SERVER_PROCESSES_H
#define LAB_2_1_SERVER_PROCESSES_H

#include <time.h>

char * get_time();

// 4.5.1
int launch_proc_bg(const char * name, const char * parameters, int uid);

std::string launch_proc(const char * name, const char * parameters, int uid);

// 4.5.2
// return list of struct?
void get_proc_info();

// 4.5.3
int watch_proc(int pid);

// 4.5.4
void watch_proc_all();

// 4.5.5
void send_sig(int pid, int sig);

// 4.5.6
// input??
void write_log(const char * info);

// 4.5.7 ??
void term_all();

// 4.5.8
int* get_sys_info();

// Logger
void log();
#endif //LAB_2_1_SERVER_PROCESSES_H
