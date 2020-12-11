I=readline;I();
N=I().split(' ').map(Number);
r=N.reduce((a,b)=>{
  A=Math.abs;
  if (A(a)<A(b)) return a;
  if (A(a)>A(b)) return b;
  return Math.max(a,b);
});
console.log(r);

// 151
I=readline;I()
N=I().split(' ').map(Number)
r=N.reduce((a,b)=>{
A=Math.abs
if(A(a)<A(b))return a
if(A(a)>A(b))return b
return Math.max(a,b)
})
print(r)

// 143
I=readline;I()
print(I().split(' ').map(Number).reduce((a,b)=>{
A=Math.abs
if(A(a)<A(b))return a
if(A(a)>A(b))return b
return Math.max(a,b)
}))
