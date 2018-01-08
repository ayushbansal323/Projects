#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <dirent.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>

typedef struct Info
{
  char name[20];
  int size;
}INFO;

int Packer(char *, char *);
int UnPacker(char *,char *);
int WritePacker(int , INFO *) ;
int WriteUnpacker(int fd1);