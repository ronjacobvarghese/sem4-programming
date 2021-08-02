#include <stdio.h>
#include <string.h>
#include <unistd.h>
#define SIZE 100
#include <ctype.h>
int main()
{
    int pfd[2];
    char buf[SIZE];
    int i = 0;
    pipe(pfd);
    if (fork())
    {
        wait(NULL);
        close(pfd[1]);
        read(pfd[0], buf, SIZE);
        while (i < strlen(buf))
        {
            buf[i] = toupper(buf[i]);
            i++;
        }
        printf("MESSAGE : %s", buf);
        close(pfd[0]);
    }
    else
    {
        close(pfd[0]);
        printf("ENTER MESSAGE : ");
        fgets(buf, sizeof(buf), stdin);
        write(pfd[1], buf, strlen(buf) + 1);
        close(pfd[1]);
    }
}   
