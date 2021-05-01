"""
https://www.codingame.com/ide/puzzle/the-river-i-
"""

def next_num(r):
    res = r
    while r:
        res += r%10
        r //=10
    return res

r1 = int(input())
r2 = int(input())

while r1 != r2:
    if r1 < r2:
        r1 = next_num(r1)
    else:
        r2 = next_num(r2)

print(r1)


"""
>>>>>>>>>>>>>>>>>>>>   Rust 


use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}


fn next_num(mut r:i64) -> i64{
    let mut res = r;
    while r>0 {
        res += r%10;
        r /=10;
    }
    return res;
}


fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let mut r1 = parse_input!(input_line, i64);
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let mut r2 = parse_input!(input_line, i64);

    while r1 != r2 {
        if r1 < r2 {r1 = next_num(r1);}
        else {r2 = next_num(r2);}
    }


    println!("{}", r1);
}



>>>>>>>>>>>>>>>>>>>>   C++


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int next_num(int r){
    int res = r;
    while (r>0){
        res += r%10;
        r /=10;
    }
    return res;
}


int main()
{
    long long r1;
    cin >> r1; cin.ignore();
    long long r2;
    cin >> r2; cin.ignore();

    while (r1 != r2){
        if (r1 < r2) r1 = next_num(r1);
        else r2 = next_num(r2);
    }

    cout << r1 << endl;
}


>>>>>>>>>>>>>>>>>>>>>>>> C

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
int next_num(int r){
    int res = r;
    while (r>0){
        res += r%10;
        r /=10;
    }
    return res;
}

int main()
{
    long long r1;
    scanf("%lld", &r1);
    long long r2;
    scanf("%lld", &r2);

    while (r1 != r2){
        if (r1 < r2) r1 = next_num(r1);
        else r2 = next_num(r2);
    }

    printf("%d\n", r1);

    return 0;
}


>>>>>>>>>>>>>>>>>>>>>>  JavaScript


var r1 = parseInt(readline());
var r2 = parseInt(readline());

function next_num(r){
    var res = r;
    while (r){
        res += r%10;
        r =parseInt(r / 10);
    }
    return res;
}

while (r1 != r2) {
    if (r1 < r2) {r1 = next_num(r1)}
    else {r2 = next_num(r2)}
}
// Write an answer using console.log()
// To debug: console.error('Debug messages...');

console.log(r1);

"""