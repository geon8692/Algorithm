n = int(input())
p = list(map(int, input().split()))

p.sort()

sum = 0
res = 0

for i in range(n):
    sum += p[i]
    if i == 0:
        res += p[i]
    else: 
        res += sum

print(res)