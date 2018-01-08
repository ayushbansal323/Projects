#include "packunpackheader.h"

int const iKey=6075;

int Packer(char *arg1, char *arg2)
{
   DIR *dir;
   struct dirent *dent ;
   char buffer[50] , name[20] ;
   strcpy(buffer,arg1);
   dir = opendir(buffer);
   int wrt;
   INFO *temp;
   if(dir == NULL)
      {
        printf("Error : opening directory");
        return 1;
      }
  int fd;

  fd = creat(arg2, 0x777  ); 
  if(fd == -1)
  {
    printf("Error : Unable to create the file\n");
  }
    chdir(buffer);
    struct  stat buf ;
    wrt = write(fd,&iKey,sizeof(iKey));
  if(wrt != sizeof(iKey))
  {
    printf("Error :Unable to write contents\n");
    return 1;
  } 
   while((dent=readdir(dir)) != NULL)
   {
      if (stat(dent->d_name, &buf) < 0)
      {
         printf("Error : while retriving statistics of file\n");
         return 1;
      }
      temp = (INFO *)malloc(sizeof(INFO)) ;
      strcpy(temp->name,dent->d_name);
      temp->size=(int)buf.st_size;
      if (S_ISREG(buf.st_mode))
      {
       if(WritePacker(fd , temp)==1)
         return 1;
      }
   }
   printf("packer is performed successfully\n");
   return 0;
}

int WritePacker(int f2 , INFO *temp) 
{   
  int f1;
  int ret , wrt;
  int offset;
  char buff[temp->size];
  int testing;
  char nouse[temp->size];
  INFO learn; 
  f1 = open(temp->name,O_RDONLY);
  if(f1 == -1)
  {
    printf("Error :Unable to open file \n");
    return 1;
  }  
  wrt = write(f2,temp,sizeof(INFO));
  if(wrt != sizeof(INFO))
  {
    printf("Error :Unable to write contents\n");
    return 1;
  }
  while((ret = read(f1,buff,temp->size)) !=0)
  {
    wrt = write(f2,buff,temp->size);
    if(wrt != temp->size)
   {
    printf("Error :Unable to write contents\n");
    return 1;
   }
  }
  return 0;
}
    

int UnPacker(char *arg1,char *arg2)
{
  int fd1 ,status,iRed,iCheckKey;
  char name[100] , buffer[100];
  strcpy(buffer,arg2);
  strcpy(name,arg1);

  fd1 = open(name,O_RDONLY);
  if(fd1 == -1)
  {
    printf("Unable to open file \n");
    return 1;
  }
  
  
  iRed=read(fd1,&iCheckKey,sizeof(iCheckKey));
  if(iCheckKey != iKey)
  {
    printf("This is not a pack file\n");
    return 1;
  }
   status = mkdir(buffer, S_IRWXU | S_IRWXG | S_IROTH |S_IXOTH );
  if(status == -1)
  {
     printf("Unable to make directory \n");
     return 1;
  }
  chdir(buffer);
  if(WriteUnpacker(fd1)==1)
    return 1;

  return 0;
}

int WriteUnpacker(int fd1 )
{
  INFO temp;
  int ret , offset , fd2,ret2;
  char *buf;
 
  while((ret = read(fd1,&temp,sizeof(INFO))) !=0)
  {
    if(ret != sizeof(INFO))
    {
       printf("Error :Unable to read contents\n");
       return 1;
    } 

    fd2 = creat(temp.name, 0x777 | S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH );
    if(fd2 == -1)
    {
      printf("Error :Unable to create the file\n");
      return 1;
    }

    
    buf=(char *)malloc(temp.size);
    ret = read(fd1,buf,temp.size);
    if(ret != temp.size)
    {
      printf("Error :Unable to read contents\n");
      return 1;
    }

    ret2 = write(fd2,buf,temp.size);
    if(ret2 != temp.size)
    {
      printf("Error :Unable to write contents\n");
      return 1;
    }
}
 printf("unpacking is performed successfully \n");
 return 0;
}









