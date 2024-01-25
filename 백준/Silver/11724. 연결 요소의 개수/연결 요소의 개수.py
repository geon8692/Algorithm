import sys

sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

result = 0

for i in range(1, N+1):
    if visited[i] is False:
        dfs(graph, i, visited)
        result += 1

print(result)