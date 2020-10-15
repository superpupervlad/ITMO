#include <stdlib.h>
#include <stdio.h>

#include "c_lib.h"

const char * get_l(){
    char *line_buf = NULL;
    size_t line_buf_size = 0;
    FILE *fp = fopen("/proc/meminfo", "r");

    ssize_t line_size = getline(&line_buf, &line_buf_size, fp);
    printf("%s %ld", line_buf, line_buf_size);
}
