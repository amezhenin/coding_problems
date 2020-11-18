#include<stdio.h>
int main(void)
{
    int i;
    while(scanf("%d",&i)>0 && i!=42)
        printf("%d\n",i);
    return 0;
} 
