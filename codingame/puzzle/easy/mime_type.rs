/**
https://www.codingame.com/training/easy/mime-type

Input
3
3
html text/html
png image/png
gif image/gif
animated.gif
portrait.png
index.html

Output
image/gif
image/png
text/html
*/


use std::io;
use std::collections::HashMap;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn alg(fname:String, exts:&HashMap<String,String>) -> String{
    //let ext = fname.split('.').next_back().unwrap();
    let mut spl = fname.split('.').collect::<Vec<_>>();
    let ext = if spl.len() > 1 { spl.pop().unwrap().to_lowercase() } else { "".to_string() };
    match exts.get(&ext) {
        Some(res) => res.to_string(),
        None => "UNKNOWN".to_string()
    }
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32); // Number of elements which make up the association table.
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let q = parse_input!(input_line, i32); // Number Q of file names to be analyzed.

    let mut exts:HashMap<String, String> = HashMap::new();

    for _ in 0..n as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let inputs = input_line.split(" ").collect::<Vec<_>>();
        let ext = inputs[0].trim().to_lowercase(); // file extension
        let mt = inputs[1].trim().to_string(); // MIME type.
        exts.insert(ext, mt);
    }
    for _ in 0..q as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let fname = input_line.trim_matches('\n').to_string(); // One file name per line.
        /* let fname = input_line.split('.').skip(1).last()
               .map_or(&u, |s| mime.get(&s.trim().to_lowercase()).unwrap_or(&u));*/
        println!("{}", alg(fname, &exts));
    }
}


