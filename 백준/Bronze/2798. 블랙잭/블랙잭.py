from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

combis = list(filter(lambda x: sum(x) <= M, list(combinations(cards, 3))))

result = 0

for combi in combis:
    if result < sum(combi):
        result = sum(combi)

print(result)