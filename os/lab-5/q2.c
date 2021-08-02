#include <stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main(){
    int a;
    float r;
    if(!fork()){
        printf("a:");
        scanf("%d",&a);
        printf("Perimeter:%d\n",4*a);
    }else{
        wait(NULL);
        printf("radius: ");
        scanf("%f",&r);
        float s=3.14*r*r;
        printf("Area: %f\n",s);
    }
    return 0;
}