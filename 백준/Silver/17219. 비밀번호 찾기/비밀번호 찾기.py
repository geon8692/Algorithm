import sys

n, m = map(int, sys.stdin.readline().split())

program = {}

for _ in range(n):
    key, value = sys.stdin.readline().split()
    program[key] = value

for _ in range(m):
    key = sys.stdin.readline().rstrip()
    print(program[key])
