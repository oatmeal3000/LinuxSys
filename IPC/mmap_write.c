#include <sys/mman.h>  
#include <sys/types.h>  
#include <fcntl.h>  
#include <unistd.h>  
  
#include <stdio.h>  
#include <string.h>  
  
typedef struct{  
    char name[4];  
    int  age;  
}people;  
  
int main(int argc, char** argv) // map a normal file as shared mem:  
{  
    int fd,i;  
    people *p_map;  
    char temp;  
      
    //open file  
    fd=open(argv[1],O_CREAT|O_RDWR|O_TRUNC,00777);  
    printf("file opened\n");  
     
    lseek(fd,sizeof(people)*5-1,SEEK_SET);  
    write(fd,"",1);  
    //create mmap  
    p_map = (people*) mmap(NULL, sizeof(people)*100, PROT_READ|PROT_WRITE, MAP_SHARED, fd, 0);  
    close( fd );  
    temp = 'a';  
    for(i=0; i<20; i++)  
    {  
        temp += 1;  
        memcpy(( *(p_map+i)).name, &temp, 1);  
        (*(p_map+i)).name[1] = 0;  
        (*(p_map+i)).age = 20+i;  
    }  
    printf("initialize over\n");  
      
    //unmap the mmap  
    sleep(10);  
    munmap((char*)p_map, sizeof(people)*100);  
    printf("umap ok\n");  
    return 0;
} 
