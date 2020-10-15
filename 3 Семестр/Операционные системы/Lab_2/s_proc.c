#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#include "s_proc.h"
#include "lib.h"

#define FILE_mem "/proc/meminfo"

// 4.5.1
int launch_proc_bg(const char * name, const char * parameters, int uid);

int launch_proc(const char * name, const char * parameters, int uid);

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
int* get_sys_info(){
    // Mem in kB
    // 1. Total mem
    // 2. Free mem
    // 3. Used mem
    // 4. CPU model
    // 5. ???
    int all_info[5];
    char * line_buf = NULL;
    size_t line_buf_size = 0;
    ssize_t line_size;
    FILE * fp = fopen(FILE_mem, "r");
    char * temps;
    int tempi;
    getline(&line_buf, &line_buf_size, fp);
    // only int
    line_buf[strlen(line_buf) - 4] = '\0';
    line_buf += 10;

    temps = trimwhitespace(line_buf);
    tempi = atoi(temps);

    all_info[0] = tempi;

    getline(&line_buf, &line_buf_size, fp);
    // only int
    line_buf[strlen(line_buf) - 4] = '\0';
    line_buf += 9;

    temps = trimwhitespace(line_buf);
    tempi = atoi(temps);

    all_info[1] = tempi;

    all_info[2] = all_info[0] - all_info[1];
}

// 4.5.9
bool check_login();
