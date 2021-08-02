#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main(){
    if(fork()){
        wait(NULL);
        if(!fork()){
            char *args[]= {"sum", "C", "Programming", NULL};
            execv("./sum", args);
        }else{
            wait(NULL);
        }
    }else{
        char *args[]={"happynewyear", "C", "Programming", NULL};
        execv("./happynewyear",args);
    }
    return 0;
}