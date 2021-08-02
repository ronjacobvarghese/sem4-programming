#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
    printf("Label -> 0 level -> 1 PID -> %d PPID -> %d\n", getpid(), getppid());
    if(!fork())
    {
        printf("Label -> 1 level -> 2 PID -> %d PPID -> %d\n", getpid(), getppid());
        if(fork()){
            wait(NULL);
            if(!fork()){
                printf("Label -> 3 level -> 3 PID -> %d PPID -> %d\n",getpid(),getppid()); 
                if(!fork()) {
                    printf("Label -> 5 level -> 4 PID -> %d PPID -> %d\n", getpid(), getppid());
                    if(fork()){
                        wait(NULL);
                        if(!fork()){
                            printf("Label -> 9 level -> 5 PID -> %d PPID -> %d\n",getpid(),getppid());
                        }
                        else{
                            wait(NULL);
                        }
                    }
                    else{
                        printf("Label -> 8 level -> 5 PID -> %d PPID -> %d\n",getpid(),getppid());
                    }
                }
                else
                    wait(NULL); 
            }
            else{
                wait(NULL);
            } 
        }
        else{
            printf("Label -> 2 level -> 3 PID -> %d PPID -> %d\n", getpid(), getppid());
            if(!fork()){
                printf("Label -> 4 level -> 4 PID -> %d PPID -> %d\n", getpid(), getppid());
                if(fork()){
                    wait(NULL); 
                    if(!fork()){
                        printf("Label -> 7 level -> 5 PID -> %d PPID -> %d\n", getpid(), getppid());
                    }
                    else{
                        wait(NULL);
                    }
                }
                else{
                    printf("Label -> 6 level -> 5 PID -> %d PPID -> %d\n", getpid(), getppid());
                }
            }
            else{
                wait(NULL); 
            }
        }
    }
    else{
        wait(NULL);
    } 
    return 0;
}
