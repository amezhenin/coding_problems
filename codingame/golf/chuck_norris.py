'''
https://www.codingame.com/ide/puzzle/chuck-norris-codesize

def alg(msg):
    """
    >>> alg("C")
    '0 0 00 0000 0 00'

    >>> alg("CC")
    '0 0 00 0000 0 000 00 0000 0 00'
    """
    bits = "".join(bin(ord(m) + 256)[4:] for m in msg)
    i = 0
    res = []
    while i < len(bits):
        flag = bits[i]
        num = 0
        while i < len(bits) and bits[i] == flag:
            i += 1
            num += 1
        res.append("0" if flag == "1" else "00")
        res.append("0" * num)
    res = " ".join(res)
    return res


if __name__ == "__main__":
    print(alg(input()))



# BEST so far 182

b="".join(bin(ord(m)+256)[4:]for m in input())
i=0
res=[]
x=len(b)
while i<x:
 f=b[i]
 n=0
 while i<x and b[i]==f:
  i+=1
  n+=1
 res+=[["0","00"][int(f)],"0"*n]
print("".join(res))
'''

b="".join(bin(ord(m)+256)[4:]for m in input())
i=0
res=[]
x=len(b)
while i<x:
 f=b[i]
 n=0
 while i<x and b[i]==f:
  i+=1
  n+=1
 res+=[["00","0"][int(f)],"0"*n]
print(" ".join(res))