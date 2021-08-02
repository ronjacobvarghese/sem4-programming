#include <stdio.h>
#include<unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>

int main()
{

    int shmid;
    int *a, *b;
    int i, n;

    shmid = shmget(IPC_PRIVATE, 2 * sizeof(int), 0777 | IPC_CREAT);

    if (fork() == 0)
    {

        b = (int *)shmat(shmid, 0, 0);
        sleep(2);

        for (i = 0; i < b[0]; i++)
        {

            if (i % 2 != 0)
            {

                printf("Child reads: %d\n", i);
            }
        }

        shmdt(b);
    }

    else
    {

        a = (int *)shmat(shmid, 0, 0);

        printf("Enter value of n: ");
        scanf("%d", &n);

        a[0] = n;
        printf("Parent writes: %d\n", n);
        wait(NULL);
        shmdt(a);
        shmctl(shmid, IPC_RMID, 0);
    }
}