"""
https://www.codingame.com/training/easy/bank-robbers
"""
r = int(input())
v = int(input())
rr = [0] * r
for i in range(v):
    c, n = [int(j) for j in input().split()]
    rr.sort()
    rr[0] += (5 ** (c - n)) * (10 ** n)

print(max(rr))
