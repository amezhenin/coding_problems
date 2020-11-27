/* Simple
#include <iostream>
#define i std::cin
#define p std::cout
int main()
{
    int x,y,h,v,t;
    i >> x >> y >> h >> v;
    for(;;) {
       i >> t;
       if (y<v) {p << "N";v-=1;}
       if (y>v) {p << "S";v+=1;}
       if (x<h) {p << "W";h-=1;}
       if (x>h) {p << "E";h+=1;}
       p << "\n";
    }
}

# Simple 205

#include <iostream>
#define i std::cin
#define p std::cout
int main(){int x,y,h,v,t;i>>x>>y>>h>>v;for(;;){i>>t;if(y<v){p<<"N";v-=1;}if(y>v){p<<"S";v+=1;}if(x<h){p<<"W";h-=1;}if(x>h){p<<"E";h+=1;}p<<"\n";}}
*/


#include <iostream>
#define i std::cin
#define p std::cout
int main(){int x,y,h,v,t;i>>x>>y>>h>>v;for(;;){i>>t;if(y<v){p<<"N";v-=1;}if(y>v){p<<"S";v+=1;}if(x<h){p<<"W";h-=1;}if(x>h){p<<"E";h+=1;}p<<"\n";}}