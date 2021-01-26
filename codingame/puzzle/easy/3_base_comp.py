"""
https://www.codingame.com/training/easy/balanced-ternary-computer-encode
"""
def inc(arr, idx):
    if arr[idx] == "T":
        arr[idx] = "0"
        return False
    if arr[idx] == "0":
        arr[idx] = "1"
        return False
    if arr[idx] == "1":
        arr[idx] = "T"
        return True

def convert(v):
    res = ['0']
    for i in range(abs(v)):
        ovf = False
        for j in range(len(res)):
            ovf = inc(res, j)
            if ovf is False:
                break
        if ovf is True:
            res = ["T"] * len(res) + ["1"]
    if v < 0:
        for j in range(len(res)):
            if res[j] == "T":
                res[j] = "1"
            elif res[j] == "1":
                res[j] = "T"
    return "".join(res[::-1])


n = int(input())
print(convert(n))
