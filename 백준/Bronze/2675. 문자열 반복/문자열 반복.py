T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    arr = [char * R for char in S]
    str = ''.join(arr)
    print(str)