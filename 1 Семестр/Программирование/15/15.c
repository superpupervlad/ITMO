#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>

void create_arc(char* filename, int number_of_files, char* files[]){
    FILE *file;
    file = fopen(filename, "w");

    unsigned char filename_size;
    unsigned int body_size;
    int i, j;
    for (i = 0; i < number_of_files; i++){
        filename_size = strlen(files[i]);
        fputc(filename_size, file); // Записали размер имени файла
        int filename_size_int = (int)filename_size;
        for (j = 0; j < filename_size_int; j++) // Записали имя файла
            fputc(files[i][j], file);
        FILE *for_archive;
        for_archive = fopen(files[i], "r"); // Открываем файл
        fseek(for_archive, 0, SEEK_END);
        body_size = ftell(for_archive);
        fseek(for_archive, 0, SEEK_SET);
        fwrite(&body_size, sizeof(unsigned int), 1, file); // Записываем размер файла
        for (j = 0; j < body_size; j++)
            fputc(getc(for_archive), file); // Записываем содержимое файла
    }
}

void get_extract(char* filename){
    FILE *file;
    file = fopen(filename, "r");
    fseek(file, 0, SEEK_END);
    unsigned int end_of_file = ftell(file);
    fseek(file, 0, SEEK_SET);
    int i;

    while(ftell(file) < end_of_file){
        unsigned int size = getc(file);
        char name_of_file[size];
        for (i = 0; i < size; i++)
            name_of_file[i] = getc(file);
        fread(&size, sizeof(unsigned int), 1, file);
        FILE *new_file;
        new_file = fopen(name_of_file, "w");
        for (i = 0; i < size; i++)
            fputc(getc(file), new_file);
        fclose(new_file);
    }
}

void get_list(char* filename){
    FILE *file;
    file = fopen(filename, "r");
    fseek(file, 0, SEEK_END);
    unsigned int end_of_file = ftell(file);
    fseek(file, 0, SEEK_SET);
    int i;

    while(ftell(file) < end_of_file){
        unsigned int size = getc(file);
        char name_of_file[size];
        for (i = 0; i < size; i++)
            name_of_file[i] = getc(file);
        printf("%s\n", name_of_file);
        fread(&size, sizeof(unsigned int), 1, file);
        fseek(file, size, SEEK_CUR);
    }
}

int main (int argc, char* argv[]){
    char normal_file[11] = "--file";
    char create[8] = "--create";
    char extract[9] = "--extract";
    char list[6] = "--list";
    char filename[20];

    strcpy(filename, argv[2]);
    if (argc > 4){
        int number_of_files = argc - 4;
        create_arc(filename, number_of_files, &argv[4]);
    }
    else if (!(strcmp(argv[3], "--extract"))){
        get_extract(filename);
    }
    else{
        get_list(filename);
    }
    printf("---------------------------\n");
    return 0;
}
//  ./15 --file data.arc --create 1.txt 2.psg 3.third
//  ./15 --file data.arc --list
//  ./15 --file data.arc --extract