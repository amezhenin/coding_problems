"""
https://www.codingame.com/training/easy/create-the-longest-sequence-of-1s

110011101111

8
"""

b = input()
s = b.split("0")
l = []
for i in range(len(s)):
    l.append(len(s[i]) + len(s[i+1]))

print(max(l)+1)