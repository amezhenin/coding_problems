"""
https://stepik.org/lesson/541855/step/2?unit=535316

Use Binary Lifting (Kth Ancestor of a Tree Node) to solve this problem

https://www.youtube.com/watch?v=oib-XsjFa-M
https://www.youtube.com/watch?v=dOAxrhAUIhA
"""
import sys
def log(msg):
    print(msg, file=sys.stderr, flush=True)

L = 19

class Alg:
    def __init__(self):
        # self.n = None
        self.up = None
        self.ic = None
        self.d = None

        self.depth = None



    def build_up(self, n):
        """
        Build binary lifting data structure
        """
        up = []
        for idx, i in enumerate(n):
            new_up = [i]
            up.append(new_up)
            for j in range(1, L+1):
                nnu = up[up[idx][j-1]][j-1]
                new_up.append(nnu)
        self.up = up


    def build_depth(self, n):
        depth = [0]
        for i in range(1, len(n)):
            depth.append(depth[n[i]] + 1)
        self.depth = depth



    def get_kth_ancestor(self, node, k):
        """
        Get K'th ancestor using binary lifting in Log(n) time (worst case)
        """
        assert type(k) == int
        for j in range(L):
            # if j-th power of 2 is in the k
            if k & (1 << j):
                node = self.up[node][j]
        return node


    def ic_lca_old(self, pq, dmi):
        # move whichever pointer is bigger up by one step
        while pq != dmi:
            if self.ic[pq] > self.ic[dmi]:
                pq = self.up[pq][0]
            else:
                dmi = self.up[dmi][0]

        return self.ic[pq]


    def ic_lca(self, a, b):
        """
        Improved version of LCA with binary lifting
        """
        # a is always lower in the tree in our case
        if self.depth[a] < self.depth[b]:
            a, b = b, a

        # pull a up until it is on the same level with b
        k = self.depth[a] - self.depth[b]
        a = self.get_kth_ancestor(a, k)

        if a == b:
            return self.ic[a]

        for j in range(L-1, -1, -1):
            if self.up[a][j] != self.up[b][j]:
                a = self.up[a][j]
                b = self.up[b][j]

        return self.ic[self.up[a][0]]


    def max_ic(self, pq, dm):

        res = list(map(lambda x: self.ic_lca(pq, x), dm))
        res = max(res)
        return res


    def calculate(self, p):
        """
        This function can be parallelized
        """
        best = None
        best_val = -1
        for dm_idx, dm in enumerate(self.d):
            # log(f"check {dm_idx}")
            cur_val = 0
            for pq in p:
                m_ic = self.max_ic(pq, dm)  # slowest <<<<<<<<<<<<<<<<<<<<
                cur_val += m_ic
            if best_val < cur_val:
                best_val = cur_val
                best = dm_idx + 1
        return best


    def run(self):
        # num of graph vertices
        _n = int(input())
        # graph parents
        n = [0] + [i-1 for i in map(int, input().split())]
        for i in range(1, _n):
            assert n[i] < i, f"{n[i]} < {i} => False"
        self.build_up(n)
        self.build_depth(n)
        self.ic = list(map(int, input().split()))

        # diseases
        _d = int(input())
        self.d = []
        for i in range(_d):
            new_d = [i-1 for i in map(int, input().split())][1:]
            self.d.append(new_d)

        # patients
        _p = int(input())
        log("Starting")
        for _pi in range(_p):
            p = [i-1 for i in map(int, input().split())][1:]

            # FIXME: run in parallel for each p
            best = self.calculate(p)
            log(f"[{_pi}/{_p}]> {best}")
            print(best)

        pass


if __name__ == "__main__":
    with open("input.txt", "r") as sys.stdin:
        with open("output.txt", "w") as sys.stdout:
            alg = Alg()
            alg.run()
    pass