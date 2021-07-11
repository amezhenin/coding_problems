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

// FIXME: vvv
#[allow(dead_code)]
fn random_policy(state: State) -> i8 {
    let mut s = state;
    while !s.is_terminal() {
        let action = s.get_random_action();
        s = s.take_action(action);
    }
    s.get_reward()
}

// FIXME: vvv
#[allow(dead_code)]
fn limit_policy(state: State) -> i8 {
    let mut s = state;
    let mut i = 0;
    while !s.is_terminal() && i < DEPTH {
        let action = s.get_random_action();
        s = s.take_action(action);
        i += 1;
    }
    s.get_reward()
}

// FIXME: vvv
#[allow(dead_code)]
struct TreeNode{
    state: State,
    is_terminal: bool,
    is_fully_expanded: bool,
    parent: Option<Box<TreeNode>>,
    children: Vec<TreeNode>,  // NOTE: for cases with large branching factor Vec should be replaced with HashMap
    num_visits: i32,
    total_reward: i32,  // NOTE: change to float if rewards are floats
}
// FIXME: vvv
#[allow(dead_code)]
impl TreeNode {
    fn new(state: State, parent: Option<Box<TreeNode>>) -> TreeNode {
        let is_terminal = state.is_terminal();
        TreeNode {
            state,
            is_terminal,
            is_fully_expanded: is_terminal,
            parent,
            children: vec![],
            num_visits: 0,
            total_reward: 0
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

    fn search(&self) -> Action {
//        while !timelimit {
//            self.execute_round()
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
    }
}
/*

class MCST:

    def search(self, initialState, needDetails=False):
        self.root = treeNode(initialState, None)

        if self.limitType == 'time':

        else:
            for i in range(self.searchLimit):
                self.executeRound()

        bestChild = self.getBestChild(self.root, 0)
        action=(action for action, node in self.root.children.items() if node is bestChild).__next__()
        if needDetails:
            return {"action": action, "expectedReward": bestChild.totalReward / bestChild.numVisits}
        else:
            log(f"Rollouts {self.root.numVisits}")
            return action

    def executeRound(self):
        """
            execute a selection-expansion-simulation-backpropagation round
        """
        node = self.selectNode(self.root)
        reward = self.rollout(node.state)
        self.backpropogate(node, reward)

    def selectNode(self, node):
        while not node.isTerminal:
            if node.isFullyExpanded:
                node = self.getBestChild(node, self.explorationConstant)
            else:
                return self.expand(node)
        return node

    def expand(self, node):
        actions = node.state.getPossibleActions()
        for action in actions:
            if action not in node.children:
                newNode = treeNode(node.state.takeAction(action), node)
                node.children[action] = newNode
                if len(actions) == len(node.children):
                    node.isFullyExpanded = True
                return newNode

        raise Exception("Should never reach here")

    def backpropogate(self, node, reward):
        while node is not None:
            node.numVisits += 1
            node.totalReward += reward
            node = node.parent

    def getBestChild(self, node, explorationValue):
        bestValue = float("-inf")
        bestNodes = []
        for child in node.children.values():
            nodeValue = node.state.getCurrentPlayer() * child.totalReward / child.numVisits + explorationValue * math.sqrt(
                2 * math.log(node.numVisits) / child.numVisits)
            if nodeValue > bestValue:
                bestValue = nodeValue
                bestNodes = [child]
            elif nodeValue == bestValue:
                bestNodes.append(child)
        return random.choice(bestNodes)
*/


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
// FIXME: vvv
#[allow(dead_code)]
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
