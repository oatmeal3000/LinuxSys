#include<stdio.h>
#include<signal.h>
#include<stdlib.h>
#include<sys/types.h>

int main()
{
    pid_t pid;
    int ret;

    if((pid = fork()) < 0){
        printf("Fork error\n");
        exit(1);
    }
    if(pid == 0){
        printf("I am child process(pid %d), waiting for signal\n", getpid());
        raise(SIGSTOP);
        printf("I am child process(pid %d), killed by %d\n", getpid(), getppid());
        exit(0);
    }
    else{
        sleep(2);
        if((waitpid(pid, NULL, WNOHANG)) == 0){
            if((ret = kill(pid, SIGKILL)) == 0) {
                printf("I am parent process(pid: %d), I killed %d\n", getpid(), pid);
            }   
        }
        waitpid(pid, NULL, 0);
        exit(0);
    }
}
