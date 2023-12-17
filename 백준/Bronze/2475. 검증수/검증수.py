list = list(map(int, input().split()))
result = sum([num**2 for num in list]) % 10
print(result)