#include <stdio.h>
#include <string.h>
#include <unistd.h>
#define SIZE 100
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
        nread=read(pfd[0],buf,SIZE);
        printf("Child read:%s\n",buf);
        close(pfd[0]);
    }
    else{
        close(pfd[0]);
        strcpy(buf,"Ron is my name,coding is not my game,today I am lame");
        write(pfd[1],buf,strlen(buf)+1);
        close(pfd[1]);
    }

}