/**
 * https://www.codingame.com/training/easy/container-terminal
 **/
use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}


fn alg(line: &str) -> usize {
    let mut stacks = vec![]; // Vec::<char>::new();
    for c in line.chars() {
        let idx = stacks.iter().position(|x| c <= *x);
        match idx {
            Some(i) => stacks[i] = c,
            None    => stacks.push(c)
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


#[test]
fn test_alg() {
    assert_eq!(alg("A"), 1);
    assert_eq!(alg("CBACBACBACBACBACBA"), 3);
    assert_eq!(alg("CCCCCBBBBBAAAAA"), 1);
    assert_eq!(alg("BDNIDPD"), 4);
    assert_eq!(alg("CODINGAME"), 4);
}
