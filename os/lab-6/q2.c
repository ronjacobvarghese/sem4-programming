#include <stdio.h>
#include <string.h>

#include <unistd.h>
#include <ctype.h>
#define SIZE 100
int main()
{

    int pfd[2];
    char num[10];
    int sum = 0, n, i, temp = 0, t = 0, buf[SIZE];

    pipe(pfd);

    if (fork())
    {

        printf("ENTER VALUES: \n");

        close(pfd[0]);

        while (1)
        {

            scanf("%s", num);
            i = 0;

            while (i < strlen(num))
            {

                if (isdigit(num[i]) == 0)
                {

                    temp = 1;
                    break;
                }
                i++;
            }

            if (temp == 1)
            {

                write(pfd[1], buf, t * sizeof(int));
                close(pfd[1]);
                printf("Found a Special Charcter\n");
                break;
            }

            n = atoi(num);
            buf[t] = n;
            t++;
        }
    }
    else
    {

        close(pfd[1]);
        t = read(pfd[0], buf, SIZE * sizeof(int));
        t = t / sizeof(int);

        for (int i = 0; i < t; i++)
        {

            sum = sum + buf[i];
        }

        printf("SUM : %d\n", sum);

        close(pfd[0]);
    }
}
