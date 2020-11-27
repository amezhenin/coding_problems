/* Simple
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

## 249
package main
import "fmt"
func main(){
var x,y,h,v,t int
fmt.Scanf("%d%d%d%d",&x,&y,&h,&v)
for{fmt.Scanf("%d",&t)
if(y<v){fmt.Printf("N");v-=1}
if(y>v){fmt.Printf("S");v+=1}
if(x<h){fmt.Printf("W");h-=1}
if(x>h){fmt.Printf("E");h+=1}
fmt.Println()}}
*/