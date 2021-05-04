/**
https://www.codingame.com/training/easy/unit-fractions
*/
use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, u64);

    for x in n+1..=2*n {
        if n*x % (x-n) == 0 {
            let y = n*x / (x-n);
            println!("1/{} = 1/{} + 1/{}", n, y, x);
        }
    }
}
