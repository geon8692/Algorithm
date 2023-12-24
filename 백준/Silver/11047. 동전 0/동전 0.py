n, k = map(int, input().split())

coins = []
cnt = 0

for _ in range(n):
    coins.append(int(input()))
coins.reverse()

for coin in coins:
    share = k // coin
    if share > 0:
        cnt += share
        k -= share * coin

print(cnt)