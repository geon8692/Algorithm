N, M = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (N+1) for _ in range(N+1)]

for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 케빈 베이컨의 수 계산
kevin_bacon = [0] * (N+1)
for i in range(1, N+1):
    for j in range(1, N+1):
        kevin_bacon[i] += graph[i][j]

# 케빈 베이컨의 수가 가장 작은 사람 찾기
min_value = INF
person = 0
for i in range(1, N+1):
    if kevin_bacon[i] < min_value:
        min_value = kevin_bacon[i]
        person = i

print(person)
