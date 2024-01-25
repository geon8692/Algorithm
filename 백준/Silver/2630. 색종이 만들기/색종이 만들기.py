N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

def cut(x, y, N):
    global white, blue
    color = paper[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                cut(x, y, N//2)
                cut(x, y + N//2, N//2)
                cut(x + N//2, y, N//2)
                cut(x + N//2, y + N//2, N//2)
                return

    if color == 1:
        blue += 1
    else:
        white += 1

cut(0, 0, N)
print(white)
print(blue)