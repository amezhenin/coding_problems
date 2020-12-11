"""
https://www.codingame.com/ide/puzzle/temperature-code-golf
"""

# 92
input()
try:print(min(map(int,input().split()),key=lambda x:abs(x)-(x>0)/2))
except:print(0)

# 77
input()
print(min(map(int,input().split()or[0]),key=lambda x:abs(x)-(x>0)/2))

# 77
I=input
I()
print(min(map(int,I().split()or[0]),key=lambda x:abs(x)-(x>0)/2))


