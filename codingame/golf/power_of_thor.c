/* Simple
#include<stdio.h>
#define s scanf
#define p print
int main()
{
    int x, y, h, v,t;
    s("%d%d%d%d", &x, &y, &h, &v);
    for(;;) {
       s("%d", &t);
       if (y<v) {p("N");v-=1;}
       if (y>v) {p("S");v+=1;}
       if (x<h) {p("W");h-=1;}
       if (x>h) {p("E");h+=1;}
       printf("\n");
    }
}

# Simple 215

#include<stdio.h>
#define s scanf
#define p printf
int main(){int x,y,h,v,t;s("%d%d%d%d",&x,&y,&h,&v);for(;;){s("%d",&t);if(y<v){p("N");v-=1;}if(y>v){p("S");v+=1;}if(x<h){p("W");h-=1;}if(x>h){p("E");h+=1;}p("\n");}}

*/
