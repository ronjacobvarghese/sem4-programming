#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
	int shmid,status,shmid1,shmid2;
	int *a, *b,*c;
	int i, *cnt, *sm, *s, *cot, *ct;

	shmid = shmget(IPC_PRIVATE, 22*sizeof(int), 0777|IPC_CREAT);
	shmid1 = shmget(IPC_PRIVATE, 1*sizeof(int), 0777|IPC_CREAT);
	shmid2 = shmget(IPC_PRIVATE, 1*sizeof(int), 0777|IPC_CREAT);
	if (fork() == 0) 
	{
		b = (int *) shmat(shmid, 0, 0);
		cnt= (int *) shmat(shmid1,0,0);
		int count = 0;
		sleep(5);
		i=0;
		while(b[i]!='\0') 
		{
			sleep(1);
			count = count + 1;
			printf("Child1 reads: %d\n",b[i]);
			i++;
			
		}
		cnt[0]=i+1;
		b[cnt[0]] = count;
		printf("%d %d\n",b[cnt[0]],cnt[0]);
		printf("Count = %d\n",count);
		
		shmdt(b);
	}
	else 
	{
		if (fork() == 0)
		{
			c = (int *) shmat(shmid, 0, 0);
			ct= (int *) shmat(shmid1,0,0);
			sm = (int *) shmat(shmid2,0,0);
			int sum = 0;
			sleep(5);
			i=0;
			while(c[i]!='\0') 
			{
				sleep(1);
				sum = sum + c[i];
				printf("Child2 reads: %d\n",c[i]);
				i++;
				
			}
			sm[0]=i+2;
			c[sm[0]] = sum;
			printf("%d %d %d\n",c[sm[0]],sm[0], c[ct[0]]);
			printf("Sum = %d\n",sum);
			
			shmdt(c);
		}
		else
		{
			a = (int *) shmat(shmid, 0, 0);
			cot =(int *) shmat(shmid1,0,0);
			s = (int *) shmat(shmid2,0,0);
			int x,i=0;
			while(scanf("%d",&x) == 1) 
			{
				a[i] = x*x;
				printf("Parent writes: %d\n",a[i]);
				i++;
			}
			a[i]='\0';
			wait(&status);
			float avg = a[s[0]]/(float)a[cot[0]];
			printf("Parent : Sum = %d \n Count= %d \n avg = %f \n",a[s[0]],a[cot[0]],avg);
			
			shmdt(a);
		}
		shmctl(shmid, IPC_RMID, 0);
	}
}