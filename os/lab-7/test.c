#include<stdio.h>

#define SIZE 1024

main(){
    int pfd[2];
    int pid;
    int nread;
    char buf;

    if(pipe(pfd)==-1){
        perror("The pipe has failed");
    }
    else if((pid=fork())<0){


    }
}