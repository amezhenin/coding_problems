/**
 * https://www.codingame.com/multiplayer/optimization/bulls-and-cows-2
 **/
use std::io;
use itertools::Itertools;
use std::time::Instant;


//static TIMEOUT: u128 = 9999999999;
static TIMEOUT: u128 = 60;
static SOFT_TIMEOUT: u128 = 40;
static WITH_COWS: bool = true;


macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}


fn read_bc() -> (i32, i32) {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let inputs = input_line.split(" ").collect::<Vec<_>>();
    let bulls = parse_input!(inputs[0], i32);
    let cows = parse_input!(inputs[1], i32);

    (bulls, cows)
}

fn match_case(src: &Vec<i32>, all_tests:&Vec<Vec<i32>>, all_bulls:&Vec<i32>, all_cows:&Vec<i32>,
              elapsed: &u128) -> (bool, bool) {
    let mut match_cows = true;
    for test_idx in 0..all_tests.len() {
        let dest = &all_tests[test_idx];
        if WITH_COWS && elapsed < &SOFT_TIMEOUT {
            let mut b = 0;
            let mut c = 0;
            for i in 0..src.len() {
                if src[i] == dest[i] {
                    b += 1;
                }
                if dest.contains(&src[i]) {
                    c += 1
                }
            }
            c -= b;
            if b != all_bulls[test_idx] {
                return (false, false)
            } else if c != all_cows[test_idx] {
                match_cows = false
            }
        } else {
            // OLD SOLUTION only with COWS
            let b = (0..src.len())
                .map(|i| (src[i] == dest[i]) as i32)
                .sum();
            if all_bulls[test_idx] != b {
                return (false, false)
            }
        }
    }
    (true, match_cows)
}


fn main() {

    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let number_length = parse_input!(input_line, usize);

    // dummy read for -1 -1
    read_bc();
    let mut timer = Instant::now();

    // algorithm
    let mut all_tests = Vec::<Vec<i32>>::new();
    let mut all_cows = Vec::<i32>::new();
    let mut all_bulls = Vec::<i32>::new();

    let num = vec![1,2,3,4,5,6,7,8,9,0];
    let cases  = num.into_iter().permutations(number_length);
    let mut last_case = vec![];

    for case in cases {
        let elapsed = timer.elapsed().as_millis();
        let (mb, mc) = match_case(&case, &all_tests, &all_bulls, &all_cows, &elapsed);
        if mb {
            last_case = case.to_vec();
            eprintln!("Last best: {:?}", &last_case);
        }
        if elapsed >= TIMEOUT || (mb && mc)  {
            eprintln!("Debug: {:?} ms", elapsed);
            println!("{}", &last_case.iter().fold(String::new(), |acc, &num| acc + &num.to_string()));

            all_tests.push(last_case.to_vec());
            // read results
            let (bulls, cows) = read_bc();
            timer = Instant::now();
            all_bulls.push(bulls);
            all_cows.push(cows);
        }
    }

}
