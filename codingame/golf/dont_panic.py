# nb_floors, width, nb_rounds, xf, xp, \
# nb_total_clones, nb_additional_elevators, nb_elevators = map(int, input().split())
#
# import sys
# def log(msg):
#     print(msg, file=sys.stderr, flush=True)

# Basic algorithm
S=list(map(int, input().split()))
el={S[3]:S[4]}
for i in range(S[-1]):
    ef, ep=map(int, input().split())
    el[ef]=ep
while True:
    inputs = input().split()
    cf = int(inputs[0])
    cp = int(inputs[1])
    d = inputs[2]
    if cf<0 or (cp <= el[cf] and d == "RIGHT") or (cp >= el[cf] and d == "LEFT"): print("WAIT")
    else: print("BLOCK")


# 237 =========================================
I,N=input,int
S=list(map(N,I().split()))
e={S[3]:S[4]}
for _ in" "*S[-1]:
 f,p=map(N,I().split())
 e[f]=p
while 1:
 i=I().split()
 f=N(i[0])
 p=N(i[1])
 d=i[2]=="RIGHT"
 print("WAIT"if f<0 or(p<=e[f]and d)or(p>=e[f]and not d)else"BLOCK")

# 249  =============================

I,N=input,int
S=list(map(N,I().split()))
e=[[S[3],S[4]],*[map(N,I().split()) for i in" "*S[-1]]]
e={k:v for k,v in e}
while 1:
 i=I().split()
 f=N(i[0])
 p=N(i[1])
 d=i[2]=="RIGHT"
 print("WAIT"if f<0 or(p<=e[f]and d)or(p>=e[f]and not d)else"BLOCK")

# BEST 228 =========================================
I,N=input,int
S=list(map(N,I().split()))
e={S[3]:S[4]}
for _ in" "*S[-1]:f,p=map(N,I().split());e[f]=p
while 1:i=I().split();f=N(i[0]);p=N(i[1]);d=i[2]=="RIGHT";print("WAIT"if f<0 or(p<=e[f]and d)or(p>=e[f]and not d)else"BLOCK")



