#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main(){
    float a;
    printf("a:");
    scanf("%f",&a);
    if(fork()){
        wait(NULL);
        if(!fork()){
            printf("perimeter of square:%f\n",4*a);
            printf("Area of square:%f",a*a);
        }
        else
        {
            wait(NULL);
        }
    }
    else{
        printf("Perimeter of the circle:%f\n",2*3.14*a);
        printf("Area of circle: %f",3.14*a*a);
    }
    return 0;
}