"""
https://www.codingame.com/ide/puzzle/skynet-revolution-episode-1
"""
from collections import defaultdict
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
links = defaultdict(list)
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    links[n1].append(n2)
    links[n2].append(n1)
log(f"Links: {links}")

exits = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    exits.append(ei)

log(f"Exits: {exits}")


def act():
    for ei in exits:
        if si in links[ei]:
            links[ei].remove(si)
            links[si].remove(ei)
            return ei, si
    for ei in exits:
        if len(links[ei]) > 0:
            p = links[ei].pop()
            links[p].remove(ei)
            return ei, p


# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    x, y = act()
    print(f"{x} {y}")
