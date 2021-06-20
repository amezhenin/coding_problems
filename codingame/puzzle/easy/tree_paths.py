"""
https://www.codingame.com/training/easy/tree-paths
"""

n = int(input())
v = int(input())
m = int(input())

parent = [-1] * (n + 1)
left = [-1] * (n + 1)
right = [-1] * (n + 1)

for i in range(m):
    p, l, r = [int(j) for j in input().split()]
    parent[l] = p
    parent[r] = p
    left[p] = l
    right[p] = r

res = []
cur = v
while parent[cur] != -1:
    par = parent[cur]
    res.append("Left" if left[par] == cur else "Right")
    cur = par

if len(res) == 0:
    res = ["Root"]

print(" ".join(res[::-1]))
