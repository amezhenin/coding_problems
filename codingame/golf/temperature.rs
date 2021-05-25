use std::io;
macro_rules! I{($x:expr,$t:ident)=>($x.trim().parse::<$t>().unwrap())}
fn main(){
 let mut l=String::new();
 io::stdin().read_line(&mut l).unwrap();
 let n=I!(l,i32);
 l.clear();
 io::stdin().read_line(&mut l).unwrap();
 let mut r=n*9999;
 for i in inputs.split_whitespace(){
  let t=I!(i,i32);
  if t.abs()<r.abs()||(t.abs()==r.abs()&&t>0){r=t;}
 }
println!("{}",r);}
