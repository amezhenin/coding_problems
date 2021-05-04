/**
https://www.codingame.com/training/medium/scrabble

Input:
5
because
first
these
could
which
hicquwh

Output:
which
*/
use std::io;
use std::collections::HashMap;


macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}


fn build_cost() -> HashMap<char, i32>{
    let mut res:HashMap<char, i32> = HashMap::new();

    res.insert('k', 5);
    for i in "eaionrtlsu".chars() {
        res.insert(i, 1);
    }
    for i in "dg".chars() {
        res.insert(i, 2);
    }
    for i in "bcmp".chars() {
        res.insert(i, 3);
    }
    for i in "fhvwy".chars() {
        res.insert(i, 4);
    }
    for i in "jx".chars() {
        res.insert(i, 8);
    }
    for i in "qz".chars() {
        res.insert(i, 10);
    }
    return res;
}


fn estimate(word:String, cost:&HashMap<char, i32>) -> i32 {
    let mut s = 0;
    for i in word.chars() {
        s += cost.get(&i).unwrap();
    }
    return s;
}


fn contains(word:String, letters:String) -> bool {
    let mut l = letters.chars().collect::<Vec<_>>();
    for w in word.chars() {
        if l.contains(&w) {
            // remove it
            let idx = l.iter().position(|&x| x == w).unwrap();
            l.remove(idx);
        } else {
            return false;
        }
    }
    return true;
}


fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);

    let words = (0..n).map(|_| {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let w = input_line.trim_matches('\n').to_string();
        w
    }).collect::<Vec<String>>();
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let letters = input_line.trim_matches('\n').to_string();

    let cost = build_cost();

    let matching = words.iter().rev()
        .filter(|x| contains(x.to_string(), letters.to_string()))
        .max_by_key(|x| estimate(x.to_string(), &cost)).unwrap();

    println!("{}", matching);
}
