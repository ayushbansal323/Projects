#include "packunpackheader.h"

int main(int argc, char *argv[])
{
   int iret;
   
   if(argc <4)
   {
         
         printf("Error : Insufficient number of command \n");
   }
   else
   {
      if(strcmp(argv[1],"-p") == 0)
      {

         iret = Packer(argv[2],argv[3]) ;
         if(iret == 1)
         {
            printf("Error : Error while performing the operation \n");
         }
      }
      else if(strcmp(argv[1],"-u") == 0)
      {
        iret = UnPacker(argv[2],argv[3]);
        if(iret == 1)
        {
           printf("Error : Error while performing the operation \n");
        }
      }
      else
      {
         printf("Error : Command not found \n");
      }
   }

   return 0;

}