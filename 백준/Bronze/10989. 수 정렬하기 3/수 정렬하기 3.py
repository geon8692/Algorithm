import sys

n = int(sys.stdin.readline())

arr = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(1, len(arr)):
    for _ in range(arr[i]):
        print(i)