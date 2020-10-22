#include <time.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#include "err_handle.h"
#include "unilib.h"

char * get_time(){
    time_t t;
    time(&t);
    return ctime(&t);
}

#define FILE_MEM "/proc/meminfo"



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
int* get_sys_info(){
    // Mem in kB
    // 1. Total mem
    // 2. Free mem
    // 3. Used mem
    // 4. CPU model
    // 5. ???
}

// 4.5.9
bool check_login();