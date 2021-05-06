"""
https://www.codingame.com/contests/spring-challenge-2021
"""

import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


COMPLETE_COST = 4

class Player:
    def __init__(self):
        self.score = 0
        self.sun = 0
        self.is_waiting = False
        self.trees = []
        self.moves = []

    def can_complete(self):
        # log(f"Can complete? sun: {self.sun} cost: {COMPLETE_COST}")
        return self.sun >= COMPLETE_COST


    def complete(self, tree):
        # log(f"Completing {tree}")
        self.sun -= COMPLETE_COST
        assert self.sun >= 0, "Out of sun"
        self.trees = list(filter(lambda x: x.idx != tree.idx, self.trees))
        return f"COMPLETE {tree.idx}"


    def can_grow(self, tree):
        if tree.size == 3:
            return False
        cost = self.grow_cost(tree)
        # log(f"Can grow {tree}? sun: {self.sun} cost: {cost}")
        return self.sun >= cost


    def grow(self, tree):
        # log(f"Growing {tree}")

        self.sun -= self.grow_cost(tree)
        assert self.sun >= 0, "Out of sun"
        # FIXME: update tree data or remove move
        return f"GROW {tree.idx}"

    def grow_cost(self, tree):
        """
        Growing a size 1 tree into a size 2 tree costs 3 sun points + the number of size 2 trees you already own.
        Growing a size 2 tree into a size 3 tree costs 7 sun points + the number of size 3 trees you already own.
        """
        assert tree.size < 3, f"Can't grow tree {tree.idx}"
        base_cost = 3 if tree.size == 1 else 7
        penalty = sum(map(lambda x: x.size == tree.size+1, self.trees))
        total = base_cost + penalty
        log(f"Cost of growing {tree.idx}: {total} ({base_cost} base + {penalty} penalty)")
        return total


class Tree:
    def __init__(self, idx, size, owner, is_dormant):
        self.idx = idx
        self.size = size
        self.owner = owner  # Player instance
        self.is_dormant = is_dormant

    def __str__(self):
        return f"Tree {self.idx}: {self.size} size"


class Game:
    def __init__(self):
        self.me = Player()
        self.enemy = Player()
        self.nutrients = 0
        self.all_trees = {}

        number_of_cells = int(input())  # 37
        for i in range(number_of_cells):
            # index: 0 is the center cell, the next cells spiral outwards
            # richness: 0 if the cell is unusable, 1-3 for usable cells
            # neigh_0: the index of the neighbouring cell for each direction
            index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
        pass


    def tree_by_move(self, move):
        idx = int(move.split(" ")[1])
        return self.all_trees[idx]


    def next_round(self):
        self.update_state()

        moves = list(filter(lambda x: x != "WAIT", self.me.moves))
        grows = list(filter(lambda x: x.startswith("GROW"), moves))
        compiles = list(filter(lambda x: x.startswith("COMPLETE"), moves))

        for move in compiles:
            if self.me.can_complete():
                tree = self.tree_by_move(move)
                print(self.me.complete(tree))
                return


        for move in grows:
            tree = self.tree_by_move(move)
            if self.me.can_grow(tree):
                print(self.me.grow(tree))
                return

        # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>
        print("WAIT")

    def update_state(self):

        day = int(input())  # the game lasts 24 days: 0-23
        log(f"Day: {day}")
        self.nutrients = int(input())  # the base score you gain from the next COMPLETE action

        # sun: your sun points
        # score: your current score
        sun, score = [int(i) for i in input().split()]
        self.me.score = score
        self.me.sun = sun
        self.me.trees = []

        inputs = input().split()
        opp_sun = int(inputs[0])  # opponent's sun points
        opp_score = int(inputs[1])  # opponent's score
        opp_is_waiting = inputs[2] != "0"  # whether your opponent is asleep until the next day
        self.enemy.score = opp_score
        self.enemy.sun = opp_sun
        self.enemy.is_waiting = opp_is_waiting
        self.enemy.trees = []

        number_of_trees = int(input())  # the current amount of trees
        for i in range(number_of_trees):
            inputs = input().split()
            cell_index = int(inputs[0])  # location of this tree
            size = int(inputs[1])  # size of this tree: 0-3
            is_mine = inputs[2] != "0"  # 1 if this is your tree
            is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
            owner = self.me if is_mine else self.enemy
            tree = Tree(cell_index, size, owner, is_dormant)
            self.all_trees[cell_index] = tree
            owner.trees.append(tree)
            log(tree)

        number_of_possible_moves = int(input())
        self.me.moves = []
        for i in range(number_of_possible_moves):
            possible_move = input()
            log(f"Move: {possible_move}")
            self.me.moves.append(possible_move)

        pass


if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()
