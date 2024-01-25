arr = input().split('-')
result = sum(list(map(int, arr[0].split('+'))))

for a in arr[1:]:
    result -= sum(list(map(int, a.split('+'))))

print(result)