N = int(input())

res = 0

for i in range(N):
    M = i + sum(list(map(int, str(i))))
    if M == N:
        res = i
        break

print(res)