/**
 * https://www.codingame.com/training/easy/container-terminal
 **/
use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}


fn alg(line: &str) -> usize {
    let mut stacks = Vec::<char>::new();
    for c in line.chars() {
        let mut idx: Option<usize> = None;
        for i in 0..stacks.len() {
            if stacks[i] >= c {
                idx = Some(i);
                break
            }
        }
        match idx {
            Some(i) => stacks[i] = c,
            None     => stacks.push(c)
        }
    }
    stacks.len()
}


fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);
    for _i in 0..n as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let line = input_line.trim_matches('\n').to_string();
        let res = alg(&line);
        println!("{}", res);
    }
}
