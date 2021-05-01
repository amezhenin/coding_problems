/*
https://www.codingame.com/training/easy/van-ecks-sequence
*/

use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let a1 = parse_input!(input_line, i32);
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);

//    let mut a:i32 = 0;
//    let n:i32 = 10;

    let mut c: [i32; 1000000] = [-1; 1000000];
    for i in 0..n-1 {
        //println!("{}", a);
        let au: usize = a as usize;

        if c[au] >= 0 {
            let ca = c[au];
            c[au] = i;
            a = i - ca;
        } else {
            c[au] = i;
            a = 0;
        }
    }

    println!("{}", a);
}
