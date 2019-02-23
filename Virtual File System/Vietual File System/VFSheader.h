#define _CRT_SECURE_NO_WARNINGS
#define MAXINODE 50
#define READ 1
#define WRITE 2
#define MAXFILESIZE 1024
#define REGULAR 1
#define SPECIAL 2
#define START 0
#define CURRENT 1
#define END 2

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<io.h>

typedef struct superblock
{
	int TotlaInodes;
	int FreeInode;
}SUPERBLOCK,*PSUPERBLOCK;
typedef struct inode
{
	char FileName[50];
	int InodeNumber;
	int FileSize;
	int FileActualSize;
	int FileType;
	char *Buffer;
	int LinkCount;
	int ReferenceCount;
	int permissions;
	struct inode *next;
}INODE,*PINODE,**PPINODE;
typedef struct filetable
{
	int readoffset;
	int writeoffset;
	int count;
	int mode;
	PINODE ptrinode;
}FILETABLE,*PFILETABLE;
typedef struct ufdt
{
	PFILETABLE ptrfiletable;
}UFDT;

void man(char *name);
void DisplayHelp();
int GetFDFromName(char *name);
PINODE GET_Inode(char *name);
void CreateDILB();
void InitialiseSuperBlock();
int CreateFile(char *name , int permissions);
int rm_File(char *name);
int ReadFile(int fd , char *arr,int isize);
int WriteFile(int fd,char *arr,int isize);
int OpenFile(char *name, int mode);
void CloseFileByFd(int fd);
int CloseFileByName(char *name);
void CloseAllFile();
int LseekFile(int fd,int size , int from);
void ls_file();
int fstat_file(int fd);
int stat_file(char *name);
int truncate_File(char *name);