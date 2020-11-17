import sys

"""
Ideas:
 * Target brew + estimate num steps to reach + evaluate by cost/num_steps
 * resources are added to the score in the end -> produce blue on the last steps
 * you can earn blue by learning first spells with tax attached tto it
 * multi cast spells that only produce 
"""


class Brew:
    def __init__(self, action_id, delta, price):
        self.action_id = action_id
        self.delta = delta
        self.price = price

    def can_use(self, inv):
        for d, i in zip(self.delta, inv):
            if d + i < 0:
                return False
        return True


class Cast:
    def __init__(self, action_id, delta, castable):
        self.action_id = action_id
        self.delta = delta
        self.castable = castable


    def can_use(self, inv):
        sum = 0
        for d, i in zip(self.delta, inv):
            if d + i < 0:
                return False
            sum += d + i
        # we can't have more than 10 items in inventory
        if sum > 10:
            return False
        return self.castable


class State:
    def __init__(self):
        self.inv = []
        self.score = 0

        self.op_inv = []
        self.op_score = 0

        self.casts = []
        self.brews = []

    def read(self):
        # reset casts and spells
        self.casts = []
        self.brews = []

        action_count = int(input())
        for i in range(action_count):

            action_id, action_type, delta_0, delta_1, delta_2, delta_3, price, tome_index, tax_count, castable, \
                repeatable = input().split()

            action_id = int(action_id)
            delta_0 = int(delta_0)
            delta_1 = int(delta_1)
            delta_2 = int(delta_2)
            delta_3 = int(delta_3)
            price = int(price)
            castable = castable != "0"
            # tome_index = int(tome_index)    # ignore in this league
            # tax_count = int(tax_count)      # ignore in this league
            # repeatable = repeatable != "0"  # ignore in this league

            if action_type == "CAST":
                cast = Cast(action_id, [delta_0, delta_1, delta_2, delta_3], castable)
                self.casts.append(cast)
            elif action_type == "BREW":
                brew = Brew(action_id, [delta_0, delta_1, delta_2, delta_3], price)
                self.brews.append(brew)
            else:
                # ignore OPPONENT_CAST for now
                pass

        *self.inv, self.score = map(int, input().split())
        *self.op_inv, self.op_score = map(int, input().split())
        pass


    def make_action(self):

        # action = ""
        # msg = ""

        for b in self.brews:
            if b.can_use(self.inv) is True:
                print("BREW %s" % b.action_id)
                return

        deficit = [0, 0, 0, 0]
        multiplier = [8, 4, 2, 1]

        for b in self.brews:
            print("Brew %s Deficit %s" % (b.delta, deficit), file=sys.stderr, flush=True)
            for idx, i, bd in zip(range(4), self.inv, b.delta):
                # i is pos, bd is neg
                d = i + bd
                # if we have deficit and it is bigger than previous, then update it
                if d < 0 and deficit[idx] < -d:
                    deficit[idx] = -d

        print("Deficit %s" % deficit, file=sys.stderr, flush=True)

        can_cast = list(filter(lambda x: x.can_use(self.inv), self.casts))
        best_cast = None
        best_def = 0
        for c in can_cast:
            # cast a spell only if it lowers the deficit * multiplier
            c_def = 0
            for d, cd, m in zip(deficit, c.delta, multiplier):
                if d > 0 and cd > 0:
                    c_def += cd * m
            print("Cast %s Score %s" % (c.delta, c_def), file=sys.stderr, flush=True)
            if c_def > best_def:
                best_def = c_def
                best_cast = c

        if best_cast:
            print("CAST %s" % best_cast.action_id)
            return

        # # FIX for a problem, when no inv_0 is needed
        # if len(can_cast) > 0:
        #     print("Force cast", file=sys.stderr, flush=True)
        #     print("CAST %s" % can_cast[0].action_id)
        #     return

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        # print("%s %s" % (action, msg))
        print("REST")


if __name__ == "__main__":
    # game loop
    state = State()

    while True:
        state.read()
        state.make_action()


