"""
https://www.codingame.com/training/easy/van-ecks-sequence
"""

a = int(input())
n = int(input())

c = {}
for i in range(n-1):
    if a in c:
        ca = c[a]
        c[a] = i
        a = i - ca
    else:
        c[a] = i
        a = 0
print(a)
