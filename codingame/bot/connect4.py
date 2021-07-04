"""
https://www.codingame.com/multiplayer/bot-programming/connect-4
"""
import sys
import random


def log(msg):
    print(msg, file=sys.stderr, flush=True)


class State:

    def __init__(self, my_id, turn, board):
        self.my_id = my_id
        self.turn = turn
        self.board = board
        self.actions = None
        self.reward = None


    def getCurrentPlayer(self):
        # 1 for maximiser, -1 for minimiser
        if self.my_id == (self.turn % 2):
            return 1
        return -1


    def getPossibleActions(self):
        if self.actions is None:
            actions = []
            for i in range(9):
                if self.board[0][i] == ".":
                    actions.append(Action(i))
            if self.turn == 1 and self.my_id == 1:
                actions.append(Action(-2))
            self.actions = actions

        return self.actions


    def takeAction(self, action):
        move = action.move
        # new_board = []
        if move == -2:
            assert self.turn == 1, "Only allowed on turn 1"
            new_board = self.board[:6]
            row = self.board[6].replace("0", "1")
            new_board.append(row)
        else:
            assert self.board[0][move] == ".", "Column is taken"
            new_board = list(self.board)
            for i in range(6, -1, -1):
                if new_board[i][move] == ".":
                    c = str(self.turn % 2)
                    new_board[i] = new_board[i][:move] + c + new_board[i][move + 1:]

        return State(self.my_id, self.turn + 1, new_board)


    def isTerminal(self):
        return self.getReward() != 0


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


    # def __eq__(self, other):
    #     raise NotImplementedError()


    def validate_actions(self, orig_actions):
        actions = self.getPossibleActions()
        try:
            assert len(actions) == len(orig_actions)
            for a, b in zip(actions, orig_actions):
                assert a.move == b
        except:
            log(f"Original actions  {orig_actions}")
            log(f"Simulated actions {actions}")
            assert False
        # log(f"Actions {actions}")


    def __repr__(self):
        res = [f"Board: {self.turn} turn, {self.getReward()} reward, terminal={self.isTerminal()}"]
        for i in self.board:
            res.append(i)
        res.append("#########")
        res.append(f"Actions: {[i.move for i in self.getPossibleActions()]}")

        return "\n".join(res)


class Action:

    def __init__(self, move):
        self.move = move


    def __eq__(self, other):
        return self.move == other.move


    def __hash__(self):
        return hash(self.move)


class Game:

    def __init__(self):
        self.turn = 0

        # my_id: 0 or 1 (Player 0 plays first)
        # opp_id: if your index is 0, this will be 1, and vice versa
        self.my_id, self.opp_id = [int(i) for i in input().split()]
        log(f"My ID: {self.my_id}")


    def next_turn(self):
        # starts from 0; As the game progresses, first player gets [0,2,4,...] and second player gets [1,3,5,...]
        self.turn = int(input())

        board = []

        for i in range(7):
            # one row of the board (from top to bottom)
            board_row = input()
            board.append(board_row)
        state = State(self.my_id, self.turn, board)
        log(state)

        num_valid_actions = int(input())  # number of unfilled columns in the board
        actions = []
        for i in range(num_valid_actions):
            action = int(input())  # a valid column index into which a chip can be dropped
            actions.append(action)
        state.validate_actions(actions)

        # opponent's previous chosen column index (will be -1 for first player in the first turn)
        opp_previous_action = int(input())

        if -2 in actions:
            print(-2)
        else:
            r = random.choice(actions)
            print(f"{r}")


if __name__ == "__main__":
    game = Game()
    while True:
        game.next_turn()


"""
def test_state_1():
    board = [
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        "........."
    ]
    state = State(0, 0, board)
    assert state.getReward() == 0

    state = State(1, 0, board)
    assert state.getReward() == 0



def test_state_2():
    board = [
        "0000.....",
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        "........."
    ]
    state = State(0, 0, board)
    assert state.getReward() == 1

    state = State(1, 0, board)
    assert state.getReward() == -1


def test_state_3():
    board = [
        "..0000...",
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        "........."
    ]
    state = State(0, 0, board)
    assert state.getReward() == 1

    state = State(1, 0, board)
    assert state.getReward() == -1



def test_state_4():
    board = [
        ".....0000",
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        "........."
    ]
    state = State(0, 0, board)
    assert state.getReward() == 1

    state = State(1, 0, board)
    assert state.getReward() == -1


def test_state_5():
    board = [
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        ".....0000"
    ]
    state = State(0, 0, board)
    assert state.getReward() == 1

    state = State(1, 0, board)
    assert state.getReward() == -1


def test_state_6():
    board = [
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        ".....1111"
    ]
    state = State(0, 0, board)
    assert state.getReward() == -1

    state = State(1, 0, board)
    assert state.getReward() == 1



def test_state_7():
    board = [
        "0........",
        "0........",
        "0........",
        "0........",
        ".........",
        ".........",
        ".........",
    ]
    state = State(0, 0, board)
    assert state.getReward() == 1

    state = State(1, 0, board)
    assert state.getReward() == -1


def test_state_8():
    board = [
        ".........",
        ".........",
        ".........",
        "........1",
        "........1",
        "........1",
        "........1"
    ]
    state = State(0, 0, board)
    assert state.getReward() == -1

    state = State(1, 0, board)
    assert state.getReward() == 1


def test_state_9():
    board = [
        "0........",
        ".0.......",
        "..0......",
        "...0.....",
        ".........",
        ".........",
        "........."
    ]
    state = State(0, 0, board)
    assert state.getReward() == 1

    state = State(1, 0, board)
    assert state.getReward() == -1


def test_state_10():
    board = [
        ".........",
        ".........",
        ".........",
        ".....1...",
        "......1..",
        ".......1.",
        "........1"
    ]
    state = State(0, 0, board)
    assert state.getReward() == -1

    state = State(1, 0, board)
    assert state.getReward() == 1


def test_state_11():
    board = [
        "........0",
        ".......0.",
        "......0..",
        ".....0...",
        ".........",
        ".........",
        "........."
    ]
    state = State(0, 0, board)
    assert state.getReward() == 1

    state = State(1, 0, board)
    assert state.getReward() == -1


def test_state_12():
    board = [
        ".........",
        ".........",
        ".........",
        "...1.....",
        "..1......",
        ".1.......",
        "1........"
    ]
    state = State(0, 0, board)
    assert state.getReward() == -1

    state = State(1, 0, board)
    assert state.getReward() == 1
"""
pass