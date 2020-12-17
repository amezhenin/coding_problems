import itertools
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)
#
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

number_length = int(input())

cases = (''.join(e) for e in itertools.permutations(iter('1234567890'), number_length))

# for the 1st round
bulls, cows = [int(i) for i in input().split()]
#log(f"{bulls} {bulls} {len(cases)}")

prev = next(cases)
print(prev)


def match(src, dest, bulls, cows):
    b = 0
    c = 0
    for i in range(number_length):
        b += src[i] == dest[i]
        c += src[i] in dest
    c = c - b
    return cows == c and bulls == b


while True:
    bulls, cows = [int(i) for i in input().split()]
    cases = filter(lambda x: match(prev, x, bulls, cows), cases)
    #log(f"{bulls} {bulls} {len(cases)}")

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # number with numberLength count of digits
    prev = next(cases)
    print(prev)
