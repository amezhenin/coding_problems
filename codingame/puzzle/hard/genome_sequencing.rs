/**
https://www.codingame.com/training/hard/genome-sequencing
*/
use std::io;
use std::cmp;
use itertools::Itertools;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, usize);

    let sub_seqs = (0..n).map(|_| {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let subseq = input_line.trim().to_string();
        subseq
    }).collect::<Vec<String>>();
    let mut best = std::usize::MAX;

    for perms in sub_seqs.into_iter().permutations(n) {
        let mut res = String::new();

        for seq in perms {
            for i in 0..=res.len(){
                let sr = cmp::min(seq.len(), res.len()-i);
                let rr = cmp::min(res.len(), i+seq.len());

                // check if we can stick new sub-sequence inside existing one
                if i + seq.len() <= res.len() {
                    if res[i..rr] == seq {
                        break;
                    }
                } else if i == res.len() || res[i..] == seq[..sr] {
                    // check and which point we can add new sub-sequence at the end
                    // of existing one. it is always possible because of `i == res.len()`
                    res += &seq[res.len()-i..];
                    break;
                }
            }
        }

        if res.len() < best {
            best = res.len()
        }
    }

    println!("{}", best);
}
