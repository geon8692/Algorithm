A = list(map(int, input()))
B = list(map(int, input()))

dp = []

for i in range(8):
    dp.append(A[i])
    dp.append(B[i])

while len(dp) != 2:
    for i in range(len(dp)-1):
        dp[i] = (dp[i] + dp[i+1]) % 10
    dp.pop()
    
print("{0}{1}".format(dp[0], dp[1]))