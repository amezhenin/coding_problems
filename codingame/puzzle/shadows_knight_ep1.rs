/**
https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1
*/
use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

#[derive(Debug)]
struct Grid {
    left: i32,
    top: i32,
    right: i32,
    bottom: i32
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let inputs = input_line.split(" ").collect::<Vec<_>>();
    let w = parse_input!(inputs[0], i32); // width of the building.
    let h = parse_input!(inputs[1], i32); // height of the building.
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32); // maximum number of turns before game over.
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let inputs = input_line.split(" ").collect::<Vec<_>>();
    let mut x = parse_input!(inputs[0], i32);
    let mut y = parse_input!(inputs[1], i32);

    let mut grid = Grid {left: 0, top: 0, right: w-1, bottom: h-1};
    eprintln!("{:?}", grid);

    // game loop
    loop {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        let bomb_dir = input_line.trim().to_string();
        eprintln!("Dir: {}", bomb_dir);

        grid = match bomb_dir.as_str() {
            "U"  => Grid {left: x,         top: grid.top, right: x,          bottom: y-1},
            "UR" => Grid {left: x+1,       top: grid.top, right: grid.right, bottom: y-1},
            "R"  => Grid {left: x+1,       top: y,        right: grid.right, bottom: y},
            "DR" => Grid {left: x+1,       top: y+1,      right: grid.right, bottom: grid.bottom},
            "D"  => Grid {left: x,         top: y+1,      right: x,          bottom: grid.bottom},
            "DL" => Grid {left: grid.left, top: y+1,      right: x-1,        bottom: grid.bottom},
            "L"  => Grid {left: grid.left, top: y,        right: x-1,        bottom: y},
            "UL" => Grid {left: grid.left, top: grid.top, right: x-1,        bottom: y-1},
            _ => panic!("Wrong direction"),
        };

        eprintln!("{:?}", grid);
        x = (grid.left + grid.right) / 2;
        y = (grid.top + grid.bottom) / 2;

        println!("{} {}", x, y);
    }
}
