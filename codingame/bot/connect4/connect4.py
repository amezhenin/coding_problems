"""
https://www.codingame.com/multiplayer/bot-programming/connect-4
"""

TIMELIMIT = 90  # 100
DEPTH = 5  # max is 63

""" ===============================   MCST algorithm   ==============================="""

# from __future__ import division

import time
import math
import random


def greedy_search(state):
    """
    Simple greedy algorithm to cover immediate loses
    """
    if state.isTerminal() is False:

        actions = state.getPossibleActions()
        state.turn += 1
        for a in actions:
            ns = state.takeAction(a)
            if ns.getReward() != 0:
                return a

    return None


def randomPolicy(state):
    while not state.isTerminal():
        try:
            action = random.choice(state.getPossibleActions())
        except IndexError:
            raise Exception("Non-terminal state has no possible actions: " + str(state))
        state = state.takeAction(action)
    return state.getReward()


def limitPolicy(state):
    """
    Test policy that does rollout only to certain depth.
    """
    i = 0
    while state.isTerminal() is False and i < DEPTH:
        try:
            action = random.choice(state.getPossibleActions())
        except IndexError:
            raise Exception("Non-terminal state has no possible actions: " + str(state))
        state = state.takeAction(action)
        i += 1
    return state.getReward()


class treeNode:
    def __init__(self, state, parent):
        self.state = state
        self.isTerminal = state.isTerminal()
        self.isFullyExpanded = self.isTerminal
        self.parent = parent
        self.numVisits = 0
        self.totalReward = 0
        self.children = {}

    def __str__(self):
        s=[]
        s.append("totalReward: %s"%(self.totalReward))
        s.append("numVisits: %d"%(self.numVisits))
        s.append("isTerminal: %s"%(self.isTerminal))
        s.append("possibleActions: %s"%(self.children.keys()))
        return "%s: {%s}"%(self.__class__.__name__, ', '.join(s))

class MCST:
    def __init__(self, timeLimit=None, iterationLimit=None, explorationConstant=1 / math.sqrt(2),
                 rolloutPolicy=randomPolicy):
        if timeLimit != None:
            if iterationLimit != None:
                raise ValueError("Cannot have both a time limit and an iteration limit")
            # time taken for each MCTS search in milliseconds
            self.timeLimit = timeLimit
            self.limitType = 'time'
        else:
            if iterationLimit == None:
                raise ValueError("Must have either a time limit or an iteration limit")
            # number of iterations of the search
            if iterationLimit < 1:
                raise ValueError("Iteration limit must be greater than one")
            self.searchLimit = iterationLimit
            self.limitType = 'iterations'
        self.explorationConstant = explorationConstant
        self.rollout = rolloutPolicy

    def search(self, initialState, needDetails=False):
        self.root = treeNode(initialState, None)

        if self.limitType == 'time':
            timeLimit = time.time() + self.timeLimit / 1000
            while time.time() < timeLimit:
                self.executeRound()
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


""" ===============================   END OF MCST algorithm   ==============================="""
import sys

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
                    break

        return State(self.my_id, self.turn + 1, new_board)


    def isTerminal(self):
        res = self.getReward() != 0 or self.getPossibleActions() == []
        return res


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

        self.mcts = MCST(timeLimit=TIMELIMIT)


    def next_turn(self):
        t = time.time()

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

        best = greedy_search(state)
        if best is None:
            best = self.mcts.search(initialState=state)
        else:
            log(f"Greedy result: {best.move}")
        t = int((time.time() - t) * 1000)
        log(f"Time: {t}")
        print(f"{best.move} {t}")


if __name__ == "__main__":
    # test_mcst_1()
    game = Game()
    while True:
        game.next_turn()




def test_mcst_1():
    board = [
        ".........",
        ".........",
        "...0.....",
        "...0.0...",
        "...0.1...",
        ".1.100...",
        "101011..."
    ]
    for i in range(2):
        state = State(i, 10+i, board)
        # state = State(1, 11, board)
        # mcts = MCST(iterationLimit=1000, rolloutPolicy=limitPolicy)
        mcts = MCST(timeLimit=100, rolloutPolicy=randomPolicy)

        best = mcts.search(initialState=state)
        assert best.move == 3

def test_mcst_2():
    board = [
        ".........",
        ".........",
        ".........",
        "..1.1....",
        "..1.0....",
        "..1.0.1..",
        "0.0.10010"
    ]
    for i in range(2):
        state = State(i, 10+i, board)
        # state = State(1, 11, board)
        # mcts = MCST(iterationLimit=1000, rolloutPolicy=limitPolicy)
        mcts = MCST(timeLimit=100, rolloutPolicy=randomPolicy)

        best = mcts.search(initialState=state)
        assert best.move == 2

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

pass