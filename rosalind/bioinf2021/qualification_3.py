"""
https://stepik.org/lesson/541855/step/2?unit=535316
"""
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)


def ic_lca(n, ic, pq, dmi):
    # move whichever pointer is bigger up by one step
    while pq != dmi:
        if ic[pq] > ic[dmi]:
            pq = n[pq]
        else:
            dmi = n[dmi]

    return ic[pq]


def max_ic(n, ic, pq, dm):

    res = list(map(lambda x: ic_lca(n, ic, pq, x), dm))
    res = max(res)
    return res


def alg():
    # num of graph vertices
    _n = int(input())
    # graph parents
    n = [-1] + [i-1 for i in map(int, input().split())]
    ic = list(map(int, input().split()))

    # diseases
    _d = int(input())
    d = []
    for i in range(_d):
        new_d = [i-1 for i in map(int, input().split())][1:]
        d.append(new_d)

    # patients
    _p = int(input())
    for _pi in range(_p):
        p = [i-1 for i in map(int, input().split())][1:]

        # calculate
        best = None
        best_val = -1
        for dm_idx, dm in enumerate(d):
            # log(f"check {dm_idx}")

            cur_val = 0
            for pq in p:
                m_ic = max_ic(n, ic, pq, dm)  # slowest <<<<<<<<<<<<<<<<<<<<
                cur_val += m_ic
            if best_val < cur_val:
                best_val = cur_val
                best = dm_idx + 1
        log(f"[{_pi}/{_p}]> {best}")
        print(best)

    pass


if __name__ == "__main__":
    with open("input.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg()
    pass