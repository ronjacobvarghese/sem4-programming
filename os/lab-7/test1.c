#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<sys/types.h>

#define SIZE 1024

int main(){
    int pfd[2];
    int pid;
    int nread;
    char buf[SIZE];

    if(pipe(pfd)==-1){
        perror("The pipe has failed");
    }
    if((pid=fork())<0){
        perror("The fork has failed");
    }
    if(pid==0){
        close(pfd[1]);
        while((nread=read(pfd[0],buf,SIZE))!=0){
            printf("Child read:%s\n",buf);
        }
        close(pfd[0]);
    }
    else{
        close(pfd[0]);
        strcpy(buf,"Ron is my name,coding is my game");
        write(pfd[0],buf,strlen(buf)+1);
        close(pfd[1]);
    }

}