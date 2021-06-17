## Javascript

var t = parseInt(readline());

var inputs = readline().split(' ');

var arr = readline().split(' ').map(Number);
var [a, b, c] = readline().split(' ').map(Number);

## C

int x, y, h, v;
scanf("%d%d%d%d", &x, &y, &h, &v);
#define s scanf
#define p print

## C++ 

int x,y,h,v,t;
cin >> x >> y >> h >> v; cin.ignore();

## Go

package main
import "fmt"
func main() {
    var x, y, h, v, t int
    fmt.Scanf("%d%d%d%d", &x, &y, &h, &v)
    for {
       fmt.Scanf("%d",&t)
       if (y<v) {fmt.Printf("N");v-=1}
       if (y>v) {fmt.Printf("S");v+=1}
       if (x<h) {fmt.Printf("W");h-=1}
       if (x>h) {fmt.Printf("E");h+=1}
       fmt.Println()
    }
}