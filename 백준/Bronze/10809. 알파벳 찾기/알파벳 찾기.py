word = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

indexs = [word.index(a) if a in word else -1 for a in alpha]
for index in indexs:
    print(index, end=' ')