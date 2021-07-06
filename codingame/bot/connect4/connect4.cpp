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
//#pragma GCC optimize "O3,omit-frame-pointer,inline"

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef char Board[7][10];


class State {
public:
    int my_id;
    int turn;
    Board* board;
//    int[] actions;
//    int reward;

    State(int my_id, int turn, Board* board){
        this->my_id = my_id;
        this->turn = turn;
        this->board = board;
//        this->actions = None
//        this->reward = None
    }
};

ostream& operator<<(ostream &out, State s)
{
    out << "Board: " << s.turn << " turn," /*<< s.get_reward()
        << " reward, terminal=" << s.is_terminal()*/ << endl;
    for (int i = 0; i < 7; i++) {
        // FIXME: why we have [0] here?
        string p(s.board[0][i]);
        out << p << endl;
    }
    out << "#########" << endl;
//    res.append(f"Actions: {[i.move for i in this->getPossibleActions()]}")
    return out;
}


class Game {
    int my_id;
    int turn;

public:
    Game() {
        // 0 or 1 (Player with ID=0 plays first)
        int oppId;
        cin >> this->my_id >> oppId;
        cin.ignore();
        cerr << "My ID: " << this->my_id << endl;
//        this->mcts = MCST(timeLimit=TIMELIMIT)
    }


    void next_turn() {
//        t = time.time()

        // starts from 0; As the game progresses, first player gets [0,2,4,...] and second player gets [1,3,5,...]
        cin >> this->turn; cin.ignore();

        Board board;
        for (auto & i : board) {
            string row; // one row of the board (from top to bottom)
            cin >> row; cin.ignore();
            for (int j = 0; j < 9; j++) {
                i[j] = row[j];
            }
            i[9] = 0;
        }
        State state(this->my_id, this->turn, &board);
        cerr << state;
//        log(state)

        int numValidActions; // number of unfilled columns in the board
        cin >> numValidActions; cin.ignore();
        for (int i = 0; i < numValidActions; i++) {
            int action; // a valid column index into which a chip can be dropped
            cin >> action; cin.ignore();
        }
        int oppPreviousAction; // opponent's previous chosen column index (will be -1 for first player in the first turn)
        cin >> oppPreviousAction; cin.ignore();

        // Output a column index to drop the chip in. Append message to show in the viewer.
        cout << "0" << endl;

        /**



        num_valid_actions = int(input())  # number of unfilled columns in the board
        actions = []
        for i in range(num_valid_actions):
            action = int(input())  # a valid column index into which a chip can be dropped
            actions.append(action)
        state.validate_actions(actions)

        # opponent's previous chosen column index (will be -1 for first player in the first turn)
        opp_previous_action = int(input())

        best = greedy_search(state)
        if best is None:
            best = this->mcts.search(initialState=state)
        else:
            log(f"Greedy result: {best.move}")
        t = int((time.time() - t) * 1000)
        log(f"Time: {t}")
        print(f"{best.move} {t}")*/
    }
};


int main() {
    Game game;
    while(1) {
        game.next_turn();
    }
    return 0;
}
