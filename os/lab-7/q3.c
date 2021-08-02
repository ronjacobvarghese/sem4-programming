#include <stdio.h> 
#include <sys/ipc.h> 
#include <sys/shm.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>    

int main() {
    int shmid,status,pid,pid2;
    int *a,*b,*c;
    shmid=shmget(IPC_PRIVATE,2*sizeof(int),0777|IPC_CREAT);
    pid=fork();
    if(pid)
        pid2=fork();
    if(!pid) {  //process 2
        b=(int*)shmat(shmid,0,0);
        while(b[1]!=1);
        b[0]=2;
        b[1]=2;
        printf("hello \n");
        shmdt(b);
    }
    else if(!pid2) {    //process 3
        c=(int*)shmat(shmid,0,0);
        while(c[1]!=2);
        c[0]=3;
        c[1]=3;
        printf("memory \n");
        shmdt(c);
    }
    else {  //process 1
        a=(int*)shmat(shmid,0,0);
        a[0]=1;
        a[1]=1;
        while(a[1]!=3);
        printf("Shared memory contains - %d \n",a[0]);
        wait(&status);
        shmdt(a);
        shmctl(shmid,IPC_RMID,0);
    }
    return 0;
}