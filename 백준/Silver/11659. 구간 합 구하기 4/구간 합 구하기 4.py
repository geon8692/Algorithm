import sys

N, M = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0]

for i in range(N):
    prefix_sum.append(prefix_sum[i] + numbers[i])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i-1])