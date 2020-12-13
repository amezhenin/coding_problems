"""
https://www.codingame.com/multiplayer/optimization/code-of-the-rings
"""
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


word = input()
log(word)

s = []
forest = [" "] * 30

for i in range(len(word)):
    fi = i % 30
    ss = ""
    # log(f"{word[i]}->{forest[fi]}")
    while forest[fi] != word[i]:
        ss += "+"
        if forest[fi] == "Z":
            new_c = " "
        elif forest[fi] == " ":
            new_c = "A"
        else:
            new_c = chr(ord(forest[fi]) + 1)
        forest[fi] = new_c
    ss += "."
    s.append(ss)

print(">".join(s))
