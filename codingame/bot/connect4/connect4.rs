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
use std::panic;
use itertools::assert_equal;
//use itertools::Itertools;


macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}


/**
 * =========================   State and Board   =========================
 * */

#[derive(Clone)]
struct Board {
    b:[[i8;9];7]
}
impl Board {
    fn read() -> Board {
        let mut board = Board { b: [[-1;9];7] };
        // read current board
        for i in 0..7 as usize {
            let mut input_line = String::new();
            io::stdin().read_line(&mut input_line).unwrap();
            // one row of the board (from top to bottom)
            let row: Vec<i8> = input_line.chars().map(|x| match x {
                '0' => 0,
                '1' => 1,
                _   => -1
            }).collect();
            for j in 0..9 as usize {
                board.b[i][j] = row[j];
            }
        }
        board
    }
    fn get(&self, row: usize, col: usize) -> i8 {
        self.b[row][col]
    }
    fn set(&mut self, row: usize, col: usize, val: i8) {
        self.b[row][col] = val;
    }

}

impl fmt::Debug for Board {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for r in 0..7 as usize {
            for c in 0..9 as usize {
                let x = match self.b[r][c] {
                    0 => '0',
                    1 => '1',
                    _ => '.'
                };
                write!(f, "{}", x)?;
            }
            writeln!(f, "")?;
        }
        writeln!(f, "#########")
    }
}


struct State {
    my_id: u8,
    turn: u8,
    board: Board
}
impl State {
    fn new(my_id: u8, turn: u8, board: Board) -> State {
        State {my_id, turn, board }
    }

    /** Interface function for MCST */
    fn get_current_player(&self) -> i32 {
        // 1 for maximiser, -1 for minimiser
        if self.my_id == (self.turn % 2) { 1 } else { -1 }
    }

    /** Interface function for MCST */
    fn get_possible_actions(&self) -> Vec<Action> {
        let mut actions:Vec<Action> = vec![];
        for i in 0..9 {
            if self.board.get(0, i) == -1 {
                actions.push(Action(i as i8))
            }
            if self.turn == 1 && self.my_id == 1 {
                actions.push(Action(-2))
            }
        }
        actions
    }

    /** Interface function for MCST */
    fn take_action(&self, action: Action) -> State {
        let new_board = if action.0 == -2 {
            // -2 is a special case where we flip opponent's move on the first turn
            assert!(self.turn == 1, "Only allowed on turn 1");
            let mut brd = self.board.clone();

            for i in 0..9 {
                let v = brd.get(6, i);
                if v != -1 {
                    // flip position with the first move
                    brd.set(6, i, 1 - v);
                    break;
                }
            }
            brd
        } else {
            // generic case, place move to the lowest possible position in the board
            let mut brd = self.board.clone();
            assert!(brd.get(0, action.0 as usize) == -1, "Column is taken");
            for i in (0..7).rev() {
                if brd.get(i, action.0 as usize) == -1 {
                    let c = (self.turn % 2) as i8;
                    brd.set(i, action.0 as usize, c);
                    break;
                }
            }
            brd
        };

        State { my_id: self.my_id, turn: self.turn + 1, board: new_board }
    }


    /**
    def getReward(self):
        # 1 for win, -1 for lose
        # check horizontal line ----
        b = self.board
        for y in range(7):
            for x in range(9 - 3):
                if b[y][x:x + 4] in ("0000", "1111"):
                    c = b[y][x]
                    res = 1 if self.my_id == int(c) else -1
                    return res

        # check vertical line |
        for y in range(7 - 3):
            for x in range(9):
                l = b[y][x] + b[y + 1][x] + b[y + 2][x] + b[y + 3][x]
                if l in ("0000", "1111"):
                    c = b[y][x]
                    res = 1 if self.my_id == int(c) else -1
                    return res

        # check diagonal line \
        for y in range(7 - 3):
            for x in range(9 - 3):
                l = b[y][x] + b[y + 1][x + 1] + b[y + 2][x + 2] + b[y + 3][x + 3]
                if l in ("0000", "1111"):
                    c = b[y][x]
                    res = 1 if self.my_id == int(c) else -1
                    return res

        # check diagonal line /
        for y in range(7 - 3):
            for x in range(9 - 3):
                l = b[y + 3][x] + b[y + 2][x + 1] + b[y + 1][x + 2] + b[y][x + 3]
                if l in ("0000", "1111"):
                    c = b[y + 3][x]
                    res = 1 if self.my_id == int(c) else -1
                    return res

        return 0


    def isTerminal(self):
        res = self.getReward() != 0 or self.getPossibleActions() == []
        return res

    */

    fn validate_actions(&self, orig_actions: Vec<Action>) {
        let actions = self.get_possible_actions();
        let res = panic::catch_unwind(|| {
            assert!(actions.len() == orig_actions.len());
            let it = actions.iter().zip(orig_actions.iter());
            for (a, b) in it {
                assert!(a.0 == b.0);
            }
        });
        if res.is_err() {
            eprintln!("Original actions  {:?}", orig_actions);
            eprintln!("Simulated actions {:?}", actions);
            panic!("Action validation failed!")
        }
        eprintln!("Actions {:?}", actions);

    }
}
impl fmt::Debug for State {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        writeln!(f, "State: {} my ID, {} turn", self.my_id, self.turn)?;
        writeln!(f, "{:?}", self.board)
    }
}


#[derive(Debug)]
struct Action(i8);


/**
 * =========================   Game   =========================
 * */


struct Game {
    my_id: u8
}
impl Game {
    fn new() -> Game{
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let inputs = input_line.split(" ").collect::<Vec<_>>();
        let my_id = parse_input!(inputs[0], u8); // 0 or 1 (Player 0 plays first)
        let _opp_id = parse_input!(inputs[1], u8); // if your index is 0, this will be 1, and vice versa

        eprintln!("My ID: {}", my_id);
        Game{my_id}
    }

    fn next_turn(&mut self) {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        // starts from 0; As the game progresses, first player gets [0,2,4,...] and second player gets [1,3,5,...]
        let turn = parse_input!(input_line, u8);

        let board = Board::read();
        let state = State::new(self.my_id, turn, board);
        eprintln!("{:?}", state);

        // read possible actions for current board
        let mut actions:Vec<Action> = vec![];

        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let num_valid_actions = parse_input!(input_line, i32);
        for _ in 0..num_valid_actions as usize {
            let mut input_line = String::new();
            io::stdin().read_line(&mut input_line).unwrap();
            let act = parse_input!(input_line, i8);
            actions.push(Action(act));
        }

        state.validate_actions(actions);

        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        // opponent's previous chosen column index (will be -1 for first player in the first turn)
        let _opp_previous_action = parse_input!(input_line, i32);


        //FIXME: best = self.mcts.search(initialState=state)
        //       t = int((time.time() - t) * 1000)
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
