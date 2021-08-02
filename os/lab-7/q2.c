#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>


int main()
{
    int shmid, status;
    char *a, *b;
    int i;

    shmid = shmget(IPC_PRIVATE, 20 * sizeof(char), 0777 | IPC_CREAT);

    if (fork() == 0)
    {
        b = (char *)shmat(shmid, 0, 0);
        sleep(10);
        i = 0;
        char word[20];
        while (b[i] != '\0')
        {
            word[i] = toupper(b[i]);
            i = i + 1;
        }
        word[i] = '\0';
        printf("%s\n", word);
        shmdt(b);
    }
    else
    {
        a = (char *)shmat(shmid, 0, 0);
        char word[20];
        scanf("%s", word);
        for (i = 0; i < 20; i++)
        {
            a[i] = word[i];
        }
        a[i] = '\0';
        
        wait(&status);
        printf("%p %d\n",&status,status);

        shmdt(a);
        shmctl(shmid, IPC_RMID, 0);
    }
}
