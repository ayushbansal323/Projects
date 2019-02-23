#include"VFSheader.h"

extern UFDT UFDTArr[50];
extern SUPERBLOCK SUPERBLOCKobj;
extern PINODE head ;


int main()
{
	char *ptr=NULL;
	int ret=0,fd=0,count=0;
	char command[4][80],str[80],arr[1024],tempstr[80];

	InitialiseSuperBlock();
	CreateDILB();

	while (1) {
		fflush(stdin);
		strcpy_s(str,"");

		printf("\nVirtual File System :>");
		fgets(str,80,stdin);
		count=sscanf(str,"%s%s%s%s",command[0],command[1],command[2],command[3]);

		if (count == 1) {
			if (_stricmp(command[0],"ls")==0) {
				ls_file();
			}
			else if (_stricmp(command[0],"closeall")==0) {
				CloseAllFile();
				printf("All File Closed Successfully\n" );
				continue;
			}
			else if (_stricmp(command[0],"clear")==0) {
				system("cls");
				continue;
			}
			else if (_stricmp(command[0],"help")==0) {
				DisplayHelp();
				continue;
			}
			else if (_stricmp(command[0],"exit")==0) {
				printf("Terminating Virtual File System Created By Ayush Agarwal\n" );
				break;
			}
			else
			{
				printf("\nError:Command not found !!!\n" );
				continue;
			}
		}
		else if (count == 2) {
			if (_stricmp(command[0],"stat")==0) {
				ret = stat_file(command[1]);
				if (ret==-1) {
					printf("ERROR : Incorrect parameters\n" );
				}
				if (ret == -2)
				{
					printf("Error : There is no such file\n" );
				}
				continue;
			}
			else if (_stricmp(command[0],"fstat")==0) {
				ret = fstat_file(atoi(command[1]));
				if (ret==-1) {
					printf("ERROR : Incorrect parameters\n" );
				}
				if (ret == -2)
				{
					printf("Error : There is no such file\n" );
				}
				continue;
			}
			else if (_stricmp(command[0],"close")==0) {
				ret = CloseFileByName(command[1]);
				if(ret == -1)
					printf("Error : There is no such file\n" );
				continue;
			}
			else if (_stricmp(command[0],"rm")==0) {
				ret = rm_File(command[1]);
				if(ret == -1)
					printf("Error : There is no such file\n" );
				continue;
			}
			else if (_stricmp(command[0],"man")==0) {
				man(command[1]);
			}
			else if (_stricmp(command[0],"write")==0) {
				fd =GetFDFromName(command[1]);
				if (fd==-1) {
					printf("Error: Incorrect parameters\n" );
					continue;
				}
				printf("Enter the data \n" );
				scanf("%s[^\n]",arr );
				ret=strlen(arr);
				if (ret == 0) {
					printf("Error : Incorrect parameters\n" );
					continue;
				}
				ret = WriteFile(fd,arr,ret);
				if (ret == -1) {
					printf("Error : Permission Denied \n");
				}
				if (ret == -2) {
					printf("Error : There is no sufficient memory to write\n" );
				}
				if (ret == -3) {
					printf("Error : It is not a regular file\n" );
				}
			}
			else if (_stricmp(command[0],"truncate")==0) {
				ret = truncate_File(command[1]);
				if (ret == -1) {
					printf("Error : Incorrect parameters\n" );
				}
			}
			else
			{
				printf("\nError : Command not Found !!! \n" );\
				continue;
			}
		}
		else if (count == 3 ) {
			if (_stricmp(command[0],"create")==0) {
				printf("%s",command[2]);
				ret = CreateFile(command[1],atoi(command[2]));
				if (ret >=0)
					printf("\nFile is successfully created with file descriptor \n" );
				if(ret == -1)
					printf("Error : Incorrect parameters\n" );
				if (ret == -2) {
					printf("Error : There is no inodes\n" );
				}
				if (ret == -3)
					printf("Error : File already Exists\n" );
				if(ret == -4)
					printf("Error : memory llocation failure\n" );
				continue;
			}
			else if (_stricmp(command[0],"open")==0) {
				ret = OpenFile(command[1],atoi(command[2]));
				if (ret >=0)
					printf("File is Successfully opened with file descriptor \n" );
				if (ret == -1)
					printf("Error : Incorrect parameters\n" );
				if(ret == -2)
					printf("Error : File not present\n" );
				if(ret == -3)
					printf("Error : Permission Denied\n" );
				continue;
			}
			else if (_stricmp(command[0],"read")==0) {
				fd = GetFDFromName(command[1]);
				if (fd == -1) {
					printf("Error : Incorrect parameters\n" );
					continue;
				}
				ptr = (char *)malloc(sizeof(atoi(command[2]))+1);
				if(ptr == NULL)
				{
					printf("Error : Incorrect parameters\n" );
					continue;
				}
				ret = ReadFile(fd,ptr,atoi(command[2]));
				if(ret == -1)
					printf("Error : File not existing\n" );
				if(ret == -2)
					printf("Error : Permission Denied\n" );
				if(ret ++ -3)
					printf("Error : Reached at the end of file\n" );
				if(ret == -4)
					printf("Error : It is not a regular file\n" );
				if(ret == 0)
					printf("Error : File empty\n" );
				if (ret > 0) {
					_write(2,ptr,ret);
				}
				continue;
			}
			else{
				printf("\nError : Command not found !!!\n" );
				continue;
			}
		}
		else if (count == 4) {
			if (_stricmp(command[0],"lseek")==0) {
				fd=GetFDFromName(command[1]);
				if (fd == -1) {
					printf("Error : Incorrect parameters\n" );
					continue;
				}
				ret = LseekFile(fd,atoi(command[2]),atoi(command[3]));
				if (ret == -1) {
					printf("Error : Unable to perform lseek\n" );
				}
			}
			else{
				printf("\nError: Command Not Found\n" );
				continue;
			}
		}
		else
		{
			printf("\nError : Command not found\n" );
			continue;
		}
	}
	return 0;
}
