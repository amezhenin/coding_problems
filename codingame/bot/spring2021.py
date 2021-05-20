#!/usr/bin/python3
"""
https://www.codingame.com/contests/spring-challenge-2021
"""
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


# final day of the game(0-indexed).
LAST_DAY = 23
# cost of completing the tree
COMPLETE_COST = 4

# # max allowed number of trees by size
# MAX_TREES = [1, 2, 2, 55]

# evaluation of the shadow in the cell
SHADOW_INFLATION = 0.95
SHADOW_OPP_PENALTY = -0.60
SHADOW_COST = 1.0
SHADOW_PARTIAL_COST = 0.65

# evaluation of moves

# COMPLETE
COMPLETE_SCALING = 1.25
# SEED
SEED_BONUS = 200
SEED_SM_TREE_PENALTY = -1000
SEED_SHADOW_PENALTY = -20
SEED_RICH_BONUS_FACTOR = 10


# # WAIT
# SUN_GAIN_FACTOR = 5  # old is 0


class Player:

    def __init__(self, pid):
        self.pid = pid
        self.score = 0
        self.sun = 0
        self.is_waiting = False
        self.trees = []
        self.moves = []
        self._tree_size = None


    def count_trees(self, size):
        # FIXME: WTF is the problem with this count !?!?!?
        if self._tree_size is None:
            # log(f"Counting for {self.trees}")
            self._tree_size = [0, 0, 0, 0]
            for i in self.trees:
                self._tree_size[i.size] += 1
            log(f"Tree sizes {self._tree_size} for {self.trees}")

        return self._tree_size[size]


    def can_complete(self):
        # log(f"Can complete? sun: {self.sun} cost: {COMPLETE_COST}")
        return self.sun >= COMPLETE_COST


    def complete(self, tree):
        # log(f"Completing {tree}")
        self.sun -= COMPLETE_COST
        assert self.sun >= 0, "Out of sun"
        # FIXME: don't change the state, create new immutable Player
        self.trees = list(filter(lambda x: x.cell_idx != tree.cell_idx, self.trees))
        return f"COMPLETE {tree.cell_idx}"


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
        # FIXME: don't change the state, create new immutable Player
        return f"GROW {tree.idx}"


    def grow_cost(self, tree):
        """
        Growing a seed into a size 1 tree costs 1 sun point + the number of size 1 trees you already own.
        Growing a size 1 tree into a size 2 tree costs 3 sun points + the number of size 2 trees you already own.
        Growing a size 2 tree into a size 3 tree costs 7 sun points + the number of size 3 trees you already own.
        """
        assert tree.size < 3, f"Can't grow tree {tree.cell_idx}"
        base_cost = [1, 3, 7][tree.size]
        penalty = self.count_trees(tree.size + 1)
        total = base_cost + penalty
        # log(f"Cost of growing {tree.cell_idx}: {total} ({base_cost} base + {penalty} penalty)")
        return total


    def can_seed(self, tree):
        cost = self.seed_cost()
        return tree.size > 0 and self.sun >= cost


    def seed_cost(self):
        penalty = sum(map(lambda x: x.size == 0, self.trees))
        # log(f"Cost of seeding: {penalty}")
        return penalty


class Tree:

    def __init__(self, cell_idx, size, owner, is_dormant):
        self.cell_idx = cell_idx
        self.__size = size
        self.owner = owner  # Player instance
        self.is_dormant = is_dormant


    @property
    def size(self):
        return self.__size

    def __repr__(self):
        return f"Tree {self.cell_idx}: {self.size} size"


class Cell:

    def __init__(self, idx, richness, links):
        self.idx = idx
        self.richness = richness
        self.links = links


    def __repr__(self):
        return f"Cell {self.idx}: {self.richness} rich"


class Game:

    def __init__(self):
        self.day = 0
        self.nutrients = 0
        self.me = Player(pid=0)
        self.enemy = Player(pid=1)
        self.all_trees = {}
        self.all_cells = {}

        number_of_cells = int(input())  # 37
        for i in range(number_of_cells):
            # index: 0 is the center cell, the next cells spiral outwards
            # richness: 0 if the cell is unusable, 1-3 for usable cells
            # links (neighbours): the index of the neighbouring cell for each direction.
            idx, richness, *links = map(int, input().split())
            # -1 means a wall
            # links = list(filter(lambda x: x != -1, links))
            cell = Cell(idx, richness, links)
            self.all_cells[idx] = cell
            # log(cell)
        pass


    def cell_shadow(self, cell, last_day=LAST_DAY):
        """
        Calculate number of times during 6 day cycle when we have shadow here
        """
        res = 0.0
        # log(f"CS {cell}")
        cache = {}
        for d in range(last_day, self.day, -1):
            res *= SHADOW_INFLATION

            if d % 6 not in cache:
                # log("Cache miss")

                next_cell = cell
                val = 0.0
                for size in range(1, 4):
                    next_idx = next_cell.links[d % 6]
                    if next_idx == -1:
                        # log(f"CS break, hit wall")
                        break

                    next_cell = self.all_cells[next_idx]
                    # log(f"CS next cell {next_cell} size {size}")
                    if next_cell.idx in self.all_trees:
                        tree = self.all_trees[next_cell.idx]
                        tree_size = tree.size
                        penalty = 0 if (tree.owner.pid == 0) else SHADOW_OPP_PENALTY
                        # treat seeds as size one trees or 0.5 increase?
                        if tree_size == 0:
                            tree_size = 1

                        if tree_size >= size:
                            val = SHADOW_COST + penalty
                            break
                        # shadow can be cased in the future by a larger tree
                        elif tree_size < 3 and tree_size + 1 == size:
                            val = (SHADOW_PARTIAL_COST + penalty)
                            break
                cache[d % 6] = val

            res += cache[d % 6]
            # log(f"Cell {cell.idx} Day {d} shadow {res}")

        # log(f"{cell} shadows {res}")
        return res


    def tree_by_move(self, move):
        idx = int(move.split(" ")[1])
        return self.all_trees[idx]


    def cell_by_move(self, move):
        idx = int(move.split(" ")[2])
        return self.all_cells[idx]


    def next_round(self):
        self.update_state()

        print(self.eval_move_strategy())


    """**********************************************************************
       ******           ALT SOLUTION: EVALUATE MOVES                   ******
    """


    def eval_move_strategy(self):
        #log("=====    EVAL MOVE strategy    =====")
        moves = []
        for move in self.me.moves:
            score = self.eval_move(move)
            moves.append((score, move))
        # log(f"^^^^^ End eval ^^^^^")

        # score DESC
        moves.sort(key=lambda x: -x[0])
        log(f"Moves: {moves}")
        return moves[0][1]


    def eval_move(self, move):
        res = 0.0

        if move.startswith("COMPLETE"):
            # this is what we will get right away
            right_now = self.complete_score(move) * 3
            # this is what we will get in dividends
            tree = self.tree_by_move(move)
            cell = self.all_cells[tree.cell_idx]
            shadow_score = self.cell_shadow(cell)

            dividends = ((LAST_DAY - self.day - shadow_score) * 3)** COMPLETE_SCALING
            res = right_now - COMPLETE_COST - dividends
            # log(f"{move}: {right_now} - 4 - {dividends} = {res}")

        elif move.startswith("GROW"):
            tree = self.tree_by_move(move)
            # investment price
            res -= self.me.grow_cost(tree)
            # this is what we will get in dividends
            tree = self.tree_by_move(move)
            cell = self.all_cells[tree.cell_idx]
            shadow_score = self.cell_shadow(cell)
            res += (LAST_DAY - self.day - shadow_score) * (tree.size + 1)

        elif move.startswith("SEED"):
            # we want free seeds
            seed_trees = self.me.count_trees(0)
            # log(f"Seed trees: {seed_trees}")
            if seed_trees == 0:
                res += SEED_BONUS
            else:
                res -= SEED_BONUS
            # don't use small trees for seeds
            tree = self.tree_by_move(move)
            if tree.size == 1:
                res += SEED_SM_TREE_PENALTY
            # take shadow and richness into consideration
            cell = self.cell_by_move(move)
            shadow_score = self.cell_shadow(cell)

            res += int(shadow_score * SEED_SHADOW_PENALTY)
            res += cell.richness * SEED_RICH_BONUS_FACTOR
            # log(f"Total {res}, {cell} shadow {int(shadow_score * SEED_SHADOW_PENALTY)}")
        else:
            assert move == "WAIT"
            # next_gain = 0
            # for i in range(1, 4):
            #     next_gain += i * self.me.count_trees(i)
            # # log(f"Next day can gain {next_gain} sun")
            # res += next_gain # * SUN_GAIN_FACTOR

        # log(f"Score: {res} Move: {move}")
        return res


    """******           ALT SOLUTION: EVALUATE MOVES                   ******
       **********************************************************************
    """


    # def max_trees(self, size):
    #     res = MAX_TREES[size]
    #     if size == 3:
    #         res = min(res, LAST_DAY - self.day)
    #     return res
    def complete_score(self, move):
        assert move.startswith("COMPLETE")
        tree = self.tree_by_move(move)
        cell = self.all_cells[tree.cell_idx]
        richness_bonus = [0, 0, 2, 4][cell.richness]
        score = self.nutrients + richness_bonus
        # log(f"Complete score for {tree} is {score}")
        return score


    def update_state(self):
        self.day = int(input())  # the game lasts 24 days: 0-23
        self.nutrients = int(input())  # the base score you gain from the next COMPLETE action
        log(f"***** Day: {self.day} Nutrients: {self.nutrients} *****")

        self.me = Player(pid=0)
        self.enemy = Player(pid=1)

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
            # log(tree)

        number_of_possible_moves = int(input())
        self.me.moves = []
        for i in range(number_of_possible_moves):
            possible_move = input()
            # log(f"Move: {possible_move}")
            self.me.moves.append(possible_move)

        pass


if __name__ == "__main__":
    game = Game()
    while True:
        game.next_round()
