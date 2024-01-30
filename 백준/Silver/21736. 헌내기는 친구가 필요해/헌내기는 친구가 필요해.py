from collections import deque

N, M = map(int, input().split())

campus = [list(input()) for _ in range(N)]

x, y = None, None
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            x, y = i, j
            break
    if x is not None:
        break

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    result = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if campus[nx][ny] == "X":
                continue
            if campus[nx][ny] == "O" or campus[nx][ny] == "P":
                if campus[nx][ny] == "P":
                    result += 1
                campus[nx][ny] = "X"
                queue.append((nx, ny))
    if result == 0:
        print("TT")
    else:
        print(result)

bfs(x, y)