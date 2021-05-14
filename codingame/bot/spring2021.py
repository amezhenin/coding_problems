"""
https://www.codingame.com/contests/spring-challenge-2021
"""
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


"""
IDEAS:
    * (!) chop more if we are falling behind in sun
    * sorting for GROW options
    * in LATE game you don't grow. only chop t3 trees last day and collect SUN 
    
    * casting shadows logic. 
        * predictions of future sun. check on next day with actual sun
    
    * generation of moves for future use. check it's output with given moves at first
    * BFS over states with current heuristic. 
        * optimization: Mid stage (max -> my_sun_produced - enemy_sun_produced)
        * optimization: Late stage (max -> my_score - enemy_score)
"""

# final day of the game(0-indexed).
LAST_DAY = 23
# cost of completing the tree
COMPLETE_COST = 4


# max allowed number of trees by size
MAX_TREES = [1, 2, 2, 5]
# day when we flip strategy to late game
LATE_GAME = 18



class Player:
    def __init__(self, pid):
        self.pid = pid
        self.score = 0
        self.sun = 0
        self.is_waiting = False
        self.trees = []
        self.moves = []

    def count_trees(self, size):
        return sum(map(lambda x: x.size == size, self.trees))

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
        penalty = self.count_trees(tree.size+1)
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
        self.size = size
        self.owner = owner  # Player instance
        self.is_dormant = is_dormant

    def __repr__(self):
        return f"Tree {self.cell_idx}: {self.size} size"


class Cell:
    def __init__(self, idx, richness, links):
        self.idx = idx
        self.richness = richness
        self.links = links

    def __repr__(self):
        return f"Cell {self.idx}: {self.richness} rich, {self.links} links"


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

    def cell_shadow(self, cell):
        """
        Calculate number of times during 6 day cycle when we have shadow here
        """
        res = 0.0
        # log(f"CS {cell}")
        for d in range(self.day, self.day+6):
            res *= 0.95         # FIXME: magic number
            next_cell = cell
            for size in range(1, 4):
                next_idx = next_cell.links[d%6]
                if next_idx == -1:
                    # log(f"CS break, hit wall")
                    break

                next_cell = self.all_cells[next_idx]
                # log(f"CS next cell {next_cell} size {size}")
                if next_cell.idx in self.all_trees:
                    tree = self.all_trees[next_cell.idx]
                    penalty = 0 if (tree.owner.pid == 0) else -0.5         # FIXME: magic number
                    # treat seeds as size one trees or 0.5 increase?
                    if tree.size == 0:
                        tree.size = 1

                    if tree.size >= size:
                        res += (1 + penalty)         # FIXME: magic number
                        break
                    # shadow can be cased in the future by a larger tree
                    elif tree.size < 3 and tree.size + 1 == size:
                        res += (0.5 + penalty)         # FIXME: magic number
                        break
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
        if self.day < LATE_GAME:
            print(self.mid_game())
        else:
            print(self.late_game())

    def max_trees(self, size):
        res = MAX_TREES[size]
        if size == 3:
            res = min(res, LAST_DAY - self.day)
        return res


    def pick_grow(self):
        # GROW: grow smaller trees first
        grows = list(filter(lambda x: x.startswith("GROW"), self.me.moves))

        best_move = None
        best_val = 999
        for move in grows:
            tree = self.tree_by_move(move)
            next_size = tree.size+1
            max_count = self.max_trees(next_size)
            cur_count = self.me.count_trees(next_size)
            # log(f"Tree count {cur_count} of size {next_size}")
            if cur_count < max_count and best_val > tree.size and self.me.can_grow(tree):
                best_move = move
                best_val = tree.size
                # log(f"New best grow: {move}")

        if best_move is not None:
            return best_move
        return None

    def pick_seed(self):
        # SEED
        seeds = list(filter(lambda x: x.startswith("SEED"), self.me.moves))

        # log(f"Tree count {self.me.count_trees(0)} of size {0}")
        if self.me.count_trees(0) < self.max_trees(0):
            best_move = []
            for move in seeds:
                tree = self.tree_by_move(move)
                cell = self.cell_by_move(move)
                cell_shadow = self.cell_shadow(cell)
                if self.me.can_seed(tree):
                    richness = cell.richness
                    best_move.append((cell_shadow, richness, move))

            # sort by shadows ASC and richness DESC
            best_move.sort(key=lambda x: (x[0], -x[1]))
            # greedy version
            #best_move.sort(key=lambda x: (-x[1], x[0]))
            # log(f"Pick seed move: {best_move}")

            if len(best_move) > 0:
                return best_move[0][2]

        return None

    # def pick_complete(self):
    #     compiles = list(filter(lambda x: x.startswith("COMPLETE"), self.me.moves))
    #
    #     # COMPLETE: harvest only when we have too much
    #     cur_max = self.max_trees(3)
    #     # log(f"Tree count of size 3: {self.me.count_trees(3)}/{cur_max} ")
    #     if self.me.count_trees(3) >= cur_max:
    #         for move in compiles:
    #             if self.me.can_complete():
    #                 tree = self.tree_by_move(move)
    #                 # log(f"Harvesting excess: {tree}")
    #                 return self.me.complete(tree)
    #     return None

    def pick_complete(self, force=False):
        compiles = list(filter(lambda x: x.startswith("COMPLETE"), self.me.moves))
        best_move = []

        # COMPLETE: harvest only when we have too much

        cur_max = 0 if force else self.max_trees(3)

        if self.me.count_trees(3) >= cur_max:
            for move in compiles:
                tree = self.tree_by_move(move)
                cell = self.all_cells[tree.cell_idx]
                cell_shadow = self.cell_shadow(cell)
                if self.me.can_complete():
                    richness = cell.richness
                    best_move.append((cell_shadow, richness, move))

        # sort by richness DESC and shadows DESC
        best_move.sort(key=lambda x: (-x[1], -x[0]))
        log(f"Chop move: {best_move}")
        if len(best_move) > 0:
            return best_move[0][2]
        return None


    def mid_game(self):
        """
        In the middle (and early) game we want to grow trees first (up to `max_trees` for sizes 1 and 2),
        then seed in the best locations(up to `max_trees`) and harvest if more than `max_trees` for size 3
        """
        log("=== MID game strategy ===")

        # alternative sequence for chopping day, COMPLETE -> SEED -> GROW

        # if we have too much pollution, we show chop all trees tomorrow
        seed_move = self.pick_seed()
        grow_move = self.pick_grow()
        complete_move = self.pick_complete()

        # default sequence
        moves = [grow_move, seed_move, complete_move]
        log(f"Regular day: {moves}")

        for move in moves:
            if move:
                return move

        return "WAIT"


    def late_game(self):
        """
        In the late game we are trying to complete trees that we have and finish growing existing trees
        """
        log("=== LATE game strategy ===")
        # COMPLETE -> GROW
        # for func in [self.pick_complete, self.pick_grow]:
        #     action = func()
        #     if action:
        #         return action

        if self.day >= LATE_GAME:
        # if self.day == LAST_DAY:
            action = self.pick_complete(force=True)
            if action:
                return action

        return "WAIT"


    def update_state(self):

        self.day = int(input())  # the game lasts 24 days: 0-23
        self.nutrients = int(input())  # the base score you gain from the next COMPLETE action
        log(f"***** Day: {self.day} Nutrients: {self.nutrients} *****")

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
