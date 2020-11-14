import sys


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
    def __init__(self, action_id, delta, price, castable):
        self.action_id = action_id
        self.delta = delta
        self.price = price
        self.castable = castable


    def can_use(self, inv):
        for d, i in zip(self.delta, inv):
            if d + i < 0:
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
                cast = Cast(action_id, [delta_0, delta_1, delta_2, delta_3], price, castable)
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

        for b in self.brews:
            print("Brew %s Deficit %s" % (b.delta, deficit), file=sys.stderr, flush=True)
            for idx, i, bd in zip(range(4), self.inv, b.delta):
                # i is pos, bd is neg
                d = i + bd
                # if we have deficit and it is bigger than previous, then update it
                if d < 0 and deficit[idx] < -d:
                    deficit[idx] = -d

        for c in self.casts:
            if c.can_use(self.inv) is True:
                # cast a spell only if it lowers the deficit
                print("Cast %s Deficit %s" % (c.delta, deficit), file=sys.stderr, flush=True)
                # FIXME: cast reset cast even when no deficit
                for d, cd in zip(deficit, c.delta):
                    if d > 0 and cd > 0:
                        print("CAST %s" % c.action_id)
                        return

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


