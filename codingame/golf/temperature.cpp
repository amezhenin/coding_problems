#include <iostream>
#include <cmath>
using namespace std;
int main(){
int n,t,r,i;
cin>>n;
r=n*9999;
for(i=0;i<n;i++){cin>>t;if(abs(t)<abs(r)or(t>0 and abs(t)==abs(r)))r=t;}
cout<<r<<endl;}