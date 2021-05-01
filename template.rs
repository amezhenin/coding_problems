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

