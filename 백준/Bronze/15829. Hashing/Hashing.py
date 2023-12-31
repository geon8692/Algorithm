L = int(input())
string = list(input())
r = 31
M = 1234567891

num = [ord(x) - 96 for x in string]
result = 0

for i in range(len(num)):
    result += num[i] * pow(r, i)
    
result %= M

print(result)