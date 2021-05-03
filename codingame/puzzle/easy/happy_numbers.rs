/**
https://www.codingame.com/training/easy/happy-numbers
*/

use std::io;
use std::collections::HashSet;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);
    for _ in 0..n as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let mut x:String = input_line.trim_matches('\n').to_string();
        let orig = x.clone();

        let mut s:HashSet<u32> = HashSet::new();
        loop {
            let mut res:u32 = 0;
            for i in x.chars() {
                res += i.to_digit(10).unwrap().pow(2);
            }
            // shortcut with lambda functions
            // let res = x.chars().map(|i| i.to_digit(10).unwrap().pow(2)).sum();
            if res == 1 {
                println!("{} :)", orig);
                break;
            } else if s.contains(&res) {
                println!("{} :(", orig);
                break;
            } else {
                s.insert(res);
                x = res.to_string();
            }
        }
    }
}


