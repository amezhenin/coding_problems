"""
https://www.codingame.com/ide/puzzle/the-lost-files

Input
13
4 10
7 2
2 1
4 1
8 10
3 9
6 3
8 0
7 4
5 10
9 6
7 0
8 5

Output
2 4
"""
from collections import defaultdict, deque


def dfs(graph, flag, cur):
    flag[cur] = True
    for v in graph[cur]:
        if flag[v] is False:
            dfs(graph, flag, v)
    pass


# def bfs(graph, start, cur, flag):
#     q = deque([cur])
#     flag[start] = True
#
#     while len(q) > 0:
#         v = q.popleft()
#         flag[v] = True
#
#         for w in graph[v]:
#             if w == start:
#                 return True
#             elif flag[w] is False:
#                 q.append(w)
#     return False


def alg(edges):
    """
    >>> alg([(1,2), (3,2), (1,3)])
    (1, 1)

    >>> alg([(1,2), (3,2), (1,3), (11,22), (33,22), (11,44), (44,33)])
    (2, 2)

    >>> alg([(4, 10), (7, 2), (2, 1), (4, 1), (8, 10), (3, 9), (6, 3), (8, 0), (7, 4), (5, 10), (9, 6), (7, 0), (8, 5)])
    (2, 4)
    """
    # max vertex ID (it is not necessarily number of vertices)
    n = max([max(e[0], e[1]) for e in edges])

    graph = defaultdict(set)
    for e in edges:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])

    flag = [False] * (n + 1)  # we need one based indexing
    c = 0
    for v in graph.keys():
        if flag[v] is False:
            c += 1
            dfs(graph, flag, v)

    t = c - len(graph) + len(edges)  # components - vertices + edges

    # there is a much simpler way to do this ^^^
    # t = 0
    # while len(graph.keys()) > 0:
    #     for v in list(graph.keys()):
    #         if v not in graph:
    #             continue
    #         if len(graph[v]) >= 2:
    #             w = graph[v].pop()
    #             graph[w].remove(v)
    #
    #             flag = [False] * (n + 1)
    #             res = bfs(graph, v, w, flag)
    #             if res is True:
    #                 t += 1
    #
    #         # clean up
    #         if len(graph[v]) == 1:
    #             w = graph[v].pop()
    #             graph[w].remove(v)
    #         if len(graph[v]) == 0:
    #             del graph[v]

    return c, t


if __name__ == "__main__":
    e = int(input())
    edges = [list(map(int, input().split())) for i in range(e)]
    res = alg(edges)
    print("%s %s" % res)
    pass
