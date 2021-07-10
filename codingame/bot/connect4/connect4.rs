/**
 * https://www.codingame.com/multiplayer/bot-programming/connect-4
 * ======== THIS CODE IS UNFINISHED ========

0 1
0
......0..
.....0...
....0....
...1.....
..1......
.1.......
1........

 * */

use std::io;
use std::fmt;
//use itertools::Itertools;


macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}


#[derive(Debug)]
struct Board {
    b:[[i8;9];7]
}
impl Board {
    fn read() -> Board {
        let mut brd = Board { b: [[-1;9];7] };
        // read current board
        for i in 0..7 as usize {
            let mut input_line = String::new();
            io::stdin().read_line(&mut input_line).unwrap();
            // one row of the board (from top to bottom)
//            let _board_row = input_line.trim().to_string();
//            let row:[char; 9] = input_line.chars()[0..9];
//            brd.b[i] = row;
            let row: Vec<i8> = input_line.chars().map(|x| match x {
                '0' => 0,
                '1' => 1,
                _   => -1
            }).collect();
            for j in 0..9 as usize {
                brd.b[i][j] = row[j];
            }
        }
        brd
    }
}


struct State {
    my_id: i32,
    turn: i32,
    brd: Board
}
impl State {
    fn new(my_id: i32, turn: i32, brd: Board) -> State {
        State {my_id, turn, brd}
    }
//    fn new(my_id: i32, turn: i32) -> State {
//        let brd = Board::read();
//        State {my_id, turn, brd}
//    }
}
impl fmt::Debug for State {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "State: {} turn\n", self.turn);
        for r in 0..7 as usize {
            for c in 0..9 as usize {
//                repr = match  { }
                let x = match self.brd.b[r][c] {
                    0 => '0',
                    1 => '1',
                    _ => '_'
                };
                write!(f, "{}", x);
            }
            write!(f, "\n");
        }
        write!(f, "#########\n")
    }
}



struct Game {
    my_id: i32
}

impl Game {
    fn new() -> Game{
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let inputs = input_line.split(" ").collect::<Vec<_>>();
        let my_id = parse_input!(inputs[0], i32); // 0 or 1 (Player 0 plays first)
        let _opp_id = parse_input!(inputs[1], i32); // if your index is 0, this will be 1, and vice versa

        eprintln!("My ID: {}", my_id);
        Game{my_id}
    }

    fn next_turn(&mut self) {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        // starts from 0; As the game progresses, first player gets [0,2,4,...] and second player gets [1,3,5,...]
        let turn = parse_input!(input_line, i32);

        let brd = Board::read();
        let state = State::new(self.my_id, turn, brd);
        eprintln!("{:?}", state);

        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let num_valid_actions = parse_input!(input_line, i32); // number of unfilled columns in the board
        for _i in 0..num_valid_actions as usize {
            let mut input_line = String::new();
            io::stdin().read_line(&mut input_line).unwrap();
            let _action = parse_input!(input_line, i32); // a valid column index into which a chip can be dropped
        }
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        // opponent's previous chosen column index (will be -1 for first player in the first turn)
        let _opp_previous_action = parse_input!(input_line, i32);


        // Output a column index to drop the chip in. Append message to show in the viewer.
        println!("0");

    }
}

fn main() {
    let mut game = Game::new();
    // game loop
    loop {
        game.next_turn();
    }
}
