import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)

result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            total += tree - mid

    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)