#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>

int main(){
    printf("label A pid=%d ppid=%d level 1\n", getpid(), getppid());
    if(!fork()){
        printf("label B pid=%d ppid=%d level 2\n", getpid(), getppid());
        if(!fork()){
            printf("label C pid=%d ppid=%d level 3\n", getpid(), getppid());
        }
        else{
            if(!fork()){
                printf("label D pid=%d ppid=%d level 3\n", getpid(), getppid());
            }
            else{
                if(!fork()){
                    printf("label E pid=%d ppid=%d level 3\n", getpid(), getppid());
                }
                else{
                    wait(NULL);
                }
            }
        }

    }
    else wait(NULL);

}