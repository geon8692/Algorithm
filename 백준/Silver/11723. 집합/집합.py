import sys
M = int(input())
S = set()
for _ in range(M):
    arr = sys.stdin.readline().split()
    command = arr[0]
    
    if len(arr) == 1:
        if command == 'all':
            S = set(range(1, 21))
        elif command == 'empty':
            S.clear() 
    else:
        x = int(arr[1])
        
        if command == 'add':
            S.add(x)
        elif command == 'remove':
            S.discard(x)
        elif command == 'check':
            print(1 if x in S else 0)
        elif command == 'toggle':
            S.discard(x) if x in S else S.add(x)