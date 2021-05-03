"""
https://www.codingame.com/training/easy/happy-numbers
"""
n = int(input())
for _ in range(n):
    x = input()
    orig = x
    s = set()
    while True:
        res = 0
        for i in x:
            res += int(i)**2
        if res == 1:
            print(f"{orig} :)")
            break
        elif res in s:
            print(f"{orig} :(")
            break
        else:
            x = str(res)
            s.add(res)
