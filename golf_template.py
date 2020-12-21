"""
I,N=input,int
for i in" "*N(I()):print(f"{N(I()):b}")

# acts like " ".join(array), but can have logic inside
f=0
for i in range(n):
 if <condition>:print(end=" "*f+f"{<something>}");f=1

# another inlined join
sentence = input().split()
print(*(sum(map('aeiouAEIOU'.count, i)) for i in sentence))

# import and assign
C=__import__("collections").Counter
"""


# convert any code into shorter version (len must be even!)
def encode(code):
    code += " " if len(code) % 2 else ""
    bcode = bytes(code, "ASCII")
    enc = bcode.decode("U16")
    res = f"exec(bytes('{enc}','U16')[2:])"
    return len(repr(res))-2, res
# print(encode(\"""<ascii code>\""")
# usage
# exec(bytes('<UTF-16 chars>','U16')[2:])


code=""""""
print(len(code))
print("%s %s" % encode(code))
