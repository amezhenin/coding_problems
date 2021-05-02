// dicts
use std::collections::HashMap;
/**
    let mut buffer: HashMap<i32, i32> = HashMap::new();
    for i in 0..end_position-1 {
        match buffer.insert(value, i) {
            None => value = 0,
            Some(x) => value = i-x,
        }
    }
*/

// read helper
fn read<T: std::str::FromStr>() -> T {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().parse().ok().unwrap()
}

fn main() {
    let mut r1: u32 = read();
    let mut r2: u32 = read();
}


/**
    // read line of ints

    let mut inputs = String::new();
    io::stdin().read_line(&mut inputs).unwrap();

    for i in inputs.split_whitespace() {
        let t = parse_input!(i, i32);
    }
*/


/*
    let inputs = input_line.split(" ").collect::<Vec<_>>();
    let x = parse_input!(inputs[0], i32);
    let y = parse_input!(inputs[1], i32);
*/


/*
#[allow(dead_code)]
*/