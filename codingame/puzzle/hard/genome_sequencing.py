"""
https://www.codingame.com/training/hard/genome-sequencing

============

Input
2
AAC
CCTT

Output
6

============

Input
3
AGATTA
GATTACA
TACAGA

Output
10

============
Input
2
AGATTA
GAT

Output
6
"""
import itertools

n = int(input())
sub_seqs = [input() for i in range(n)]

best = 999

for perms in itertools.permutations(sub_seqs):
    res = ""
    for seq in perms:
        for i in range(0, len(res)+1):
            # check if we can stick new sub-sequence inside existing one
            if i + len(seq) <= len(res):
                if res[i:i+len(seq)] == seq:
                    break
            # check and which point we can add new sub-sequence at the end
            # of existing one. it is always possible because of `0, len(res)+1`-range
            elif res[i:] == seq[:len(res)-i]:
                res += seq[len(res)-i:]
                break
    if len(res) < best:
        best = len(res)

print(best)
