#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>

union file_header {
    char buffer[10];

    struct{
        char isid3[3]; //3
        char version; // 1
        char subversion; // 1
        char flag; // 1
        char size[4]; // 4
    }data;
};

union tag_header {
    char buffer[10];

    struct{
        char tag_name[4]; // 4
        char size[4]; // 4
        char flags[2]; // 2
    }data;
};

int GetSize(char* size, int bit){
    int res = 0, k = 0, i, j, d, byte;
    for(i = 0; i < 4; i++){
        byte = size[3 - i];
        for(j = 0; j < bit; j++){
            d = (byte & 1);
            res += d * pow(2, k);
            byte = byte >> 1;
            k++;
        }
    }
    return res;
}

void get_tag(char *filename, char *tag){
    FILE *file;
    file = fopen(filename, "rb");
    union file_header file_header;
    fread(file_header.buffer, sizeof(char), 10, file);
    int i, tag_size, file_size = GetSize(file_header.data.size, 7);

    while (ftell(file) < file_size + 10){
        union tag_header tag_header;
        fread(tag_header.buffer, sizeof(char), 10, file);
        tag_size = GetSize(tag_header.data.size, 8);

        if (!(strcmp(tag, tag_header.data.tag_name))){
            char* info = malloc(sizeof(char) * tag_size);
            fread(info, sizeof(char), tag_size, file);
            printf("INFO FOR TAG %s: ", tag);
            for (i = 0; i < tag_size; i++)
                printf("%c", info[i]);
            printf("\n");
            return;
        }
        else
            fseek(file, tag_size, SEEK_CUR);
    }
}

void show(char *filename){
    FILE *file;
    file = fopen(filename, "rb");
    union file_header file_header;
    fread(file_header.buffer, sizeof(char), 10, file);
    int i, tag_size, file_size = GetSize(file_header.data.size, 7);

    while (ftell(file) < file_size + 10){
        union tag_header tag_header;
        fread(tag_header.buffer, sizeof(char), 10, file);

        printf("TAG: %s ", tag_header.data.tag_name);
        tag_size = GetSize(tag_header.data.size, 8);
        char* info = malloc(sizeof(char) * tag_size);
        fread(info, sizeof(char), tag_size, file);

        printf("- INFO: ");
        for (i = 0; i < tag_size; i++)
            printf("%c", info[i]);
        printf("\n");
        free(info);
    }
    fclose(file);
}

void set_tag(char *filename, char *tag, char *new_tag){
    FILE *file;
    file = fopen(filename, "rb");

    fseek(file, 0, SEEK_END);
    long int end_of_file = ftell(file);
    fseek(file, 0, SEEK_SET);

    union file_header file_header;
    fread(file_header.buffer, sizeof(char), 10, file);

    int new_tag_size = strlen(new_tag), i, check_for_edited = 0;
    int tag_size, file_size = GetSize(file_header.data.size, 7);
    int c;
    FILE *new_file;
    new_file = fopen("temp.mp3", "w");

    union file_header new_file_header;
    for (i = 0; i < 10; i++)
        new_file_header.buffer[i] = file_header.buffer[i];
    fseek(file, -10, SEEK_CUR);
    for (int j = 0; j < 10; j++){
        c = getc(file);
        fputc(c, new_file);
    }
    while (ftell(file) < file_size + 10){
        union tag_header tag_header;
        fread(tag_header.buffer, sizeof(char), 10, file);
        tag_size = GetSize(tag_header.data.size, 8);

        if (!(strcmp(tag, tag_header.data.tag_name))){
            check_for_edited = 1;
            union tag_header new_tag_header;
            for (i = 0; i < 10; i++)
                new_tag_header.buffer[i] = tag_header.buffer[i];
            //FILE SIZE
            int new_file_size = file_size - tag_size + new_tag_size;
            new_file_header.buffer[6] = (char)(new_file_size >> 24) & 0x0fffffff;
            new_file_header.buffer[7] = (char)(new_file_size >> 16) & 0x0fffffff;
            new_file_header.buffer[8] = (char)(new_file_size >> 8) & 0x0fffffff;
            new_file_header.buffer[9] = (char)new_file_size & 0x0fffffff;
            //TAG SIZE
            new_tag_header.buffer[4] = (char)(new_tag_size >> 24) & 0x0fffffff;
            new_tag_header.buffer[5] = (char)(new_tag_size >> 16) & 0x0fffffff;
            new_tag_header.buffer[6] = (char)(new_tag_size >> 8) & 0x0fffffff;
            new_tag_header.buffer[7] = (char)new_tag_size & 0x0fffffff;

            for (i = 0; i < 10; i++)
                fputc(new_tag_header.buffer[i], new_file);

            for (i = 0; i < new_tag_size; i++)
                fputc(new_tag[i], new_file);

            fseek(file, tag_size, SEEK_CUR);
        }
        else{
            fseek(file, -10, SEEK_CUR);
            for (int j = 0; j < tag_size + 10; j++){
                c = getc(file);
                fputc(c, new_file);
            }
        }
    }
    if (check_for_edited == 1){
        long int temp_seek = ftell(new_file);
        fseek(new_file, 6, SEEK_SET);
        fwrite(&new_file_header.buffer[6], sizeof(char), 4, new_file);
        fseek(new_file, temp_seek, SEEK_SET);
    }

    while (ftell(file) < end_of_file){
        c = getc(file);
        fputc(c, new_file);
    }

    fclose(new_file);
    rename("temp.mp3", filename);
}

int main (int argc, char* argv[]){
    char normal_filepath[11] = "--filepath=";
    char get[6] = "--get=";
    char set[6] = "--set=";
    char filename[20];
    char tag[100];
    char new_tag[50];
    int check = 1;
    for (int i=0; i < 11; i++)
        if (!(argv[1][i] == normal_filepath[i]))
            return 0;
    strcpy(filename, &argv[1][11]);

    if(!(strcmp(argv[2], "--show")))
        show(filename);
    else{
        for (int i=0; i < 6; i++)
            if (!(argv[2][i] == get[i]))
                check = 0;
        if (check == 1){
            strcpy(tag, &argv[2][6]);
            get_tag(filename, tag);
            return 0;
        }
    }
    check = 1;
    for (int i=0; i < 6; i++)
            if (!(argv[2][i] == set[i]))
                check = 0;
    if (check == 1){
        strcpy(tag, &argv[2][6]);
        strcpy(new_tag, &argv[3][8]);
        set_tag(filename, tag, new_tag);
    }
    printf("---------------------------\n");
    return 0;
}
//  ./13 --filepath=1.mp3 --show
//  ./13 --filepath=1.mp3 --get=TIT2
//  ./13 --filepath=1.mp3 --set=TIT2 --value=test
//  ./13 --filepath=1.mp3 --get=TIT2