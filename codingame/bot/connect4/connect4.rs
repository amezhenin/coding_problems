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


TODO:
    * tests
    * MCTS
    * best child: do we need 2.0 here ?

 * */

use std::io;
use std::fmt;
use std::panic;
use std::time::SystemTime;
use rand::Rng;
//use rand::seq::SliceRandom;
//use itertools::Itertools;

//const TIMELIMIT:i32 = 90;  // 100
const DEPTH:i32 = 5;  // max is 63
const EXPLORATION:f32 = 0.7;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}


/**
 * Simple greedy algorithm to cover immediate loses
 * */
fn greedy_search(state: State) -> Action {
    let actions = state.get_possible_actions();

    // let opponent move twice
    let mut s = state.clone();
    s.turn += 1;
    for a in actions {
        let ns = s.take_action(a);
        if ns.get_reward() != 0 {
            return a
        }
    }
    state.get_random_action()
}

/* Helper function that incapsulates random number generations (for possible tweaks) */
fn random_choice(actions: Vec<Action>) -> Option<Action> {
    if actions.len() == 0 {
        return None
    }
    let mut rng = rand::thread_rng();
    let idx = rng.gen_range(0..actions.len());
    Some(actions[idx])
}


/**
 * =========================   Monte-Carlo Tree Search (MCTS)  =========================
 * */

fn random_policy(state: &State) -> i8 {
    let mut s = state;
    let mut tmp:State;  // lifetime hack?
    while !s.is_terminal() {
        let action = s.get_random_action();
        tmp = s.take_action(action);
        s = &tmp;
    }
    s.get_reward()
}

//fn limit_policy(state: &State) -> i8 {
//    let mut s = state;
//    let mut i = 0;
//    while !s.is_terminal() && i < DEPTH {
//        let action = s.get_random_action();
//        s = &s.take_action(action);
//        i += 1;
//    }
//    s.get_reward()
//}

//#[derive(Clone)]
struct TreeNode{
    state: State,
    is_terminal: bool,
    is_expanded: bool,
    parent: Option<Box<TreeNode>>,
    children: Vec<TreeNode>,  // NOTE: for cases with large branching factor Vec should be replaced with HashMap
    num_visits: i32,
    total_reward: i32,  // NOTE: change to float if rewards are floats
}
impl TreeNode {
    fn new(state: State, parent: Option<Box<TreeNode>>) -> TreeNode {
        let is_terminal = state.is_terminal();
        TreeNode {
            state,
            is_terminal,
            is_expanded: is_terminal,
            parent,
            children: vec![],
            num_visits: 0,
            total_reward: 0
        }
    }

    fn expand(&mut self) {
        if !self.is_expanded {
            let actions = self.state.get_possible_actions();
            for a in actions {
                let child_state = self.state.take_action(a);
//                let parent = Some(Box::new(self));      // FIXME: references or clones? <<<<<<<<<<<<<<<<<<<<<<<
//                let child_node = TreeNode::new(child_state, parent);
                // FIXME: placeholder, see two lines above
                let child_node = TreeNode::new(child_state, None);
                self.children.push(child_node);

            }
            self.is_expanded = true;
        }
        //self.children[0] // FIXME: do we need to return anything here?
    }


    fn backpropagate(&mut self, reward: i32) {
        self.num_visits += 1;
        self.total_reward += reward;
        if let Some(n) = &mut self.parent {
            n.backpropagate(reward);  // FIXME: is it working?
        }
    }
}


struct MCTS {
    timelimit_ms: i32,
    root: TreeNode
}
impl MCTS {
    fn new(timelimit_ms: i32, init_state: State) -> MCTS {
        // FIXME(future):
        //      support iteration limit
        //      custom exploration constant
        //      custom rollout policy
        MCTS {
            timelimit_ms,
            root: TreeNode::new(init_state, None)
        }
    }

//    fn search(&self) -> Action {
//        let t1 = SystemTime::now();
//
//        while t1.elapsed().unwrap().as_millis() < (self.timelimit_ms as u128) {
//            self.execute_round();
//        }

        /*
        timeLimit = time.time() + self.timeLimit / 1000
            while time.time() < timeLimit:
                self.executeRound()

        bestChild = self.getBestChild(self.root, 0)
        action=(action for action, node in self.root.children.items() if node is bestChild).__next__()
        if needDetails:
            return {"action": action, "expectedReward": bestChild.totalReward / bestChild.numVisits}
        else:
            log(f"Rollouts {self.root.numVisits}")
            return action
        */
//    }



    /**
     *  execute a selection-expansion-simulation-backpropagation round
     * */
    fn execute_round(&mut self) {
        let root = &mut self.root;
        let node = MCTS::select_node(root);
        let reward = 1;//random_policy(&node.state);
        node.backpropagate(reward as i32);
    }

    fn select_node<'a>(start: &'a mut TreeNode) -> &'a mut TreeNode {
//        let node = start;
//        while !node.is_terminal {
//            if node.is_expanded {
//                let tmp = MCTS::get_best_child(node, EXPLORATION);
//                node = &mut tmp;
//            } else {
//                node.expand();
//                return &mut (node.children[0]);
//            }
//        }
//        return node
        if start.is_expanded {
            let tmp = MCTS::get_best_child(start, EXPLORATION);
            return MCTS::select_node(tmp);
        }
        start.expand();
        return &mut (start.children[0]);
    }


    fn get_best_child(node: &TreeNode, exploration_value: f32) -> &mut TreeNode {
        let mut best_val:f32 = std::f32::MAX;
        // FIXME: track multiple best nodes
        // let mut best_nodes: Vec<TreeNode> = vec![];
        let mut best_node:Option<&mut TreeNode> = None;

        let plr:f32 = node.state.get_current_player() as f32;
        let nnvl:f32 = (node.num_visits as f32).ln();  // natural log
        for mut child in &node.children {
            // FIXME: do we need 2.0 here ?
            let cur_val:f32 = plr * child.total_reward as f32 / child.num_visits as f32
                + exploration_value * (2.0 * nnvl / child.num_visits as f32).sqrt();
            if cur_val > best_val {
                best_val = cur_val;
                best_node = Some(&mut child);
                // best_nodes = vec![child];
            } /* else if cur_val == best_val {
                best_nodes.push(child);
            }*/
        }
        // random_choice(best_nodes)
        &mut best_node.unwrap()
    }
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

#[derive(Clone)]
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

    /* Helper function for random policy and greedy_search */
    fn get_random_action(&self) -> Action {
        let actions = self.get_possible_actions();
        if let Some(action) = random_choice(actions) {
            return action;
        }
        panic!("State has no possible actions: {:?}", self)
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
     * Interface function for MCST
     * Checks if any player has a winning combination on the board.
     * 1 - you win. -1 - you lose, 0 - otherwise
     * */
    fn get_reward(&self) -> i8 {
        let mut l:[i8;4] = [0, 0, 0, 0];
        let b = &self.board;

        // check horizontal line ----
        for y in 0..7 {
            for x in 0..9-3 {
                l[0] = b.get(y, x + 0); l[1] = b.get(y, x + 1);
                l[2] = b.get(y, x + 2); l[3] = b.get(y, x + 3);
                if l == [0, 0, 0, 0] || l == [1, 1, 1, 1] {
                    let res = if self.my_id == l[0] as u8 { 1 } else { -1 };
                    return res;
                }
            }
        }

        // check vertical line |
        for y in 0..7-3 {
            for x in 0..9 {
                l[0] = b.get(y + 0, x); l[1] = b.get(y + 1, x);
                l[2] = b.get(y + 2, x); l[3] = b.get(y + 3, x);
                if l == [0, 0, 0, 0] || l == [1, 1, 1, 1] {
                    let res = if self.my_id == l[0] as u8 { 1 } else { -1 };
                    return res;
                }
            }
        }

        // check diagonal line \
        for y in 0..7-3 {
            for x in 0..9-3 {
                l[0] = b.get(y + 0, x + 0); l[1] = b.get(y + 1, x + 1);
                l[2] = b.get(y + 2, x + 2); l[3] = b.get(y + 3, x + 3);
                if l == [0, 0, 0, 0] || l == [1, 1, 1, 1] {
                    let res = if self.my_id == l[0] as u8 { 1 } else { -1 };
                    return res;
                }
            }
        }

        // check diagonal line /
        for y in 0..7-3 {
            for x in 0..9-3 {
                l[0] = b.get(y + 3, x + 0); l[1] = b.get(y + 3, x + 1);
                l[2] = b.get(y + 1, x + 2); l[3] = b.get(y + 0, x + 3);
                if l == [0, 0, 0, 0] || l == [1, 1, 1, 1] {
                    let res = if self.my_id == l[0] as u8 { 1 } else { -1 };
                    return res;
                }
            }
        }

        // default result
        0
    }

    /**
     * Interface function for MCST
     * Indicates the final state of the game.
     * Win/Lose or no available moves
     * */
    fn is_terminal(&self) -> bool {
       self.get_reward() != 0 || self.get_possible_actions().len() == 0
    }


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


#[derive(Debug,Clone,Copy)]
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
        let t1 = SystemTime::now();

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


        let ms = t1.elapsed().unwrap().as_millis();
        let action = greedy_search(state);
        // number of visits/rollouts/simulations from the root node
        let rs = 555;
        println!("{} {} ms, {} rs", action.0, ms, rs);

    }
}

fn main() {
    let mut game = Game::new();
    // game loop
    loop {
        game.next_turn();
    }
}
