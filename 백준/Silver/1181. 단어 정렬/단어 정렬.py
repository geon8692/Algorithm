n = int(input())
words = list({input() for _ in range(n)})

words.sort()
words.sort(key=len)

for word in words:
    print(word)