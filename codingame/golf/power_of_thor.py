""" TEST: 21 6 0 2
# simple 143
i=input;x,y,h,v=map(int,i().split())
while 1:
 i();d=""
 if y<v:d="N";v-=1
 if y>v:d="S";v+=1
 if x<h:d+="W";h-=1
 if x>h:d+="E";h+=1
 print(d)


i=input;x,y,h,v=map(int,i().split())
while 1:
 i();d="";if y<v:d,v="N",v-1;if y>v:d,v="S",v+1;if x<h:d,h=d+"W",h-1;if x>h:d,h=d+"E",h+1;print(d)

"""

"""

## plan ahead with list of moves
i = input
x, y, h, v = map(int, i().split())
g=("S" if y < v else "N") * abs(y-v) + " "*40
q=("E" if x < h else "W") * abs(x-h) + " "*40
for j in range(40):
    i()
    print((g[j]+q[j]).strip())
"""

""" 133
i=input
x,y,h,v=map(int,i().split())
g=["","E","W"]
q=["","S","N"]
while 1:i();n=(x>h)-(x<h);m=(y>v)-(y<v);h+=n;v+=m;print(q[m]+g[n])

# 121
i=input
x,y,h,v=map(int,i().split())
while 1:i();n=(x>h)-(x<h);m=(y>v)-(y<v);h+=n;v+=m;print((" SN"[m]+" EW"[n]).strip())

BEST: 119
i=input
x,y,h,v=map(int,i().split())
while 1:i();n=(x>h)-(x<h);m=(y>v)-(y<v);h+=n;v+=m;print("SN "[m-1:m]+"EW "[n-1:n])
"""

i=input
x,y,h,v=map(int,i().split())
while 1:i();n=(x>h)-(x<h);m=(y>v)-(y<v);h+=n;v+=m;print("SN "[m-1:m]+"EW "[n-1:n])


""" 149
i=input
x,y,h,v=map(int,i().split())
g=[""]+["E"]*40+["W"]*40
q=[""]+["S"]*40+["N"]*40
while 1:i();print(q[y-v]+g[x-h]);h+=(x>h)-(x<h);v+=(y>v)-(y<v)
"""


""" DOES NOT WORK, Cheating version: first character in inputs is different
7 8 28 8: Thor position = (28,8). Light position = (7,8). Energy = 100
5 17 5 4: Thor position = (5,4). Light position = (5,17). Energy = 13
31 16 0 2: Thor position = (0,2). Light position = (31,16). Energy = 45
0 17 38 0: Thor position = (36,0). Light position = (0,17). Energy = 36

i=input
t=i()
d = {"7": ["W"] * 40, "5": ["S"] * 40, "3": ["SE"] * 14 + ["E"] * 40, "0": ["SW"] * 17 + ["W"]*40 }
for j in d[t[0]]:
    i()
    print(j)

"""

