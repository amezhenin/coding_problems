/**
 * https://www.codingame.com/training/easy/create-the-longest-sequence-of-1s
 *
 * 110011101111 => 8
 */
use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}


fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let b = input_line.trim_matches('\n').to_string();


    let s:Vec<i32> = b.split("0").map(|x| x.len() as i32).collect();
    let l:Vec<i32> = (0..s.len()-1).map(|i| s[i] + s[i+1] + 1).collect();

    // eprintln!("{:?}", l);
    println!("{}", l.iter().max().unwrap());
}