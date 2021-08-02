#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include <ctype.h>
#define SIZE 100
int main()
{
	int p2fd[2],p1fd[2],c1fd[2],c2fd[2];
	char num[10];
	int sum = 0,n,i,temp=0,pos=0,count;
	int write_val[SIZE], read_val[SIZE];
	pipe(p1fd);
	pipe(p2fd);
	pipe(c1fd);
	pipe(c2fd);
	if (fork())
	{
		printf("ENTER VALUES\n");
		while(1)
		{
			scanf("%s",num);
			i =0;
			while(i<strlen(num))
			{
				if(isdigit(num[i]) == 0)
				{
					temp=1;
					break;
				}
				i++;
			}
			if(temp == 1)
			{
				write(p1fd[1],write_val,pos*sizeof(int));
				close(p1fd[1]);
				write(p2fd[1],write_val,pos*sizeof(int));
				close(p2fd[1]);
				printf("SPECIAL CHARACTER FOUND\n");
				break;
			}
			n = atoi(num);
			write_val[pos]=n*n;
			pos++;
		}
		if(fork())
		{
			close(c1fd[1]);
			read(c1fd[0],&sum,sizeof(int));
			close(c1fd[0]);
			close(c2fd[1]);
			read(c2fd[0],&count,sizeof(int));
			close(c2fd[0]);
			printf("MEAN OF SQUARE OF NUMBER IS %.2f\n",(float)sum/count);
		}
		else
		{
			close(p1fd[1]);
			count = read(p1fd[0],read_val,SIZE*sizeof(int));
			close(p1fd[0]);
			count = count/sizeof(int);
			printf("COUNT : %d \n", count);
			close(c2fd[0]);
			write(c2fd[1],&count,sizeof(int));
			close(c2fd[1]);
		}
	}
	else
	{
		close(p2fd[1]);
		pos =read(p1fd[0],read_val,SIZE*sizeof(int));
		close(p1fd[0]);
		pos = pos/sizeof(int);
		for(int i=0;i<pos;i++)
		{
			sum = sum + read_val[i];
		}
	
		printf("SUM : %d\n",sum);
		close(c1fd[0]);
		write(c1fd[1],&sum,sizeof(int));
		close(c1fd[1]);
		}
	}