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
      
    int main(int argc, char** argv)  // map a normal file as shared mem:  
    {  
        int fd,i;  
        people *p_map;  
          
        //open file  
        fd=open( argv[1],O_CREAT|O_RDWR,00777 );  
          
        //create mmap and read  
        p_map = (people*)mmap(NULL,sizeof(people)*100, PROT_READ|PROT_WRITE, MAP_SHARED,fd,0);  
        for(i = 0;i<20;i++)  
        {  
            printf( "name: %s age %d;\n",(*(p_map+i)).name, (*(p_map+i)).age );  
        }  
          
        //unmap  
        munmap((char*)p_map,sizeof(people)*100);  
        return 0;
    }  
