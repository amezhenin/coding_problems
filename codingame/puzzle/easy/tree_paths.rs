/**
 * https://www.codingame.com/training/easy/tree-paths
 * */
use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let v = parse_input!(input_line, i32);
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let m = parse_input!(input_line, i32);

    let mut parent:Vec<i32> = vec![-1; (n+1) as usize];
    let mut left:Vec<i32> = vec![-1; (n+1) as usize];
    let mut right:Vec<i32> = vec![-1;  (n+1) as usize];

    for _i in 0..m as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let inputs = input_line.split(" ").collect::<Vec<_>>();
        let p = parse_input!(inputs[0], i32);
        let l = parse_input!(inputs[1], i32);
        let r = parse_input!(inputs[2], i32);
        parent[l as usize] = p;
        parent[r as usize] = p;
        left[p as usize] = l;
        right[p as usize] = r;
    }

    let mut cur = v;
    let mut res:Vec<String> = Vec::new();
    while parent[cur as usize] != -1 {
        let par = parent[cur as usize];
        let nres = if left[par as usize] == cur { "Left" } else { "Right" };
        res.push(nres.to_string());
        cur = par;
    }

    if res.len() == 0 {
        res.push("Root".to_string());
    }

    res = res.into_iter().rev().collect();
    println!("{}", res.join(" "));
}
