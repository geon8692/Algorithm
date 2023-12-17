import sys

N, M = map(int, sys.stdin.readline().split())
book = {}
book_reverse = {}
num = 0
for _ in range(N):
    num += 1
    name = sys.stdin.readline().rstrip()
    book[num] = name
    book_reverse[name] = num

for _ in range(M):
    question = sys.stdin.readline().rstrip()
    if question.isnumeric():
        print(book[int(question)])
    else:
        print(book_reverse[question])