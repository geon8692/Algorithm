T = int(input())

for _ in range(T):
    n = int(input())
    
    clothes = {}
    result = 1
    for _ in range(n):
        val, key = input().split()
        if key not in clothes:
            clothes[key] = [val]
        else: 
            clothes[key] += [val]
    
    for key in clothes:
        result *= len(clothes[key]) + 1
    
    print(result - 1)