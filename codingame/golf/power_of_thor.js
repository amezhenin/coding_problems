/* Simple
var i=readline;
var [x, y, h, v] = i().split(' ').map(Number);
for(;;) {
   i();
   d="";
   if (y<v) {d="N";v-=1}
   if (y>v) {d="S";v+=1}
   if (x<h) {d+="W";h-=1}
   if (x>h) {d+="E";h+=1}
   console.log(d);
}
# Simple 164
i=readline;[x,y,h,v]=i().split(' ').map(Number);for(;;){i();d="";if(y<v){d="N";v-=1};if (y>v){d="S";v+=1};if(x<h){d+="W";h-=1};if(x>h){d+="E";h+=1};console.log(d);}

# TypeScript version 176
let i=readline;let [x,y,h,v]=i().split(' ').map(Number);for(;;){i();let d="";if(y<v){d="N";v-=1};if (y>v){d="S";v+=1};if(x<h){d+="W";h-=1};if(x>h){d+="E";h+=1};console.log(d);}

*/

/*
i=readline;[x,y,h,v]=i().split(' ').map(Number);
g=["W","","E"];
q=["N","","S"];
for(;;){i();n=(x>h)-(x<h);m=(y>v)-(y<v);h+=n;v+=m;console.log(q[m+1]+g[n+1])}

# 155
i=readline;[x,y,h,v]=i().split(' ').map(Number);g=["W","","E"];q=["N","","S"];for(;;){i();n=(x>h)-(x<h);m=(y>v)-(y<v);h+=n;v+=m;console.log(q[m+1]+g[n+1])}


i=readline;[x,y,h,v]=i().split(' ').map(Number);
for(;;){i();n=(x>h)-(x<h);m=(y>v)-(y<v);h+=n;v+=m;console.log(("N S"[m+1]+"W E"[n+1]).trim())}


# BEST 142
i=readline;[x,y,h,v]=i().split(' ').map(Number);for(;;){i();n=(x>h)-(x<h);m=(y>v)-(y<v);h+=n;v+=m;console.log(("N S"[m+1]+"W E"[n+1]).trim())}
*/

i=readline;[x,y,h,v]=i().split(' ').map(Number);for(;;){i();n=(x>h)-(x<h);m=(y>v)-(y<v);h+=n;v+=m;console.log(("N S"[m+1]+"W E"[n+1]).trim())}