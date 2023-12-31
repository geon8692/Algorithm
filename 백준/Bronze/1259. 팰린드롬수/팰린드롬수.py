while True:
    n = list(input())
    if n[0] == '0':
        break
    if n == list(reversed(n)):
        print('yes')
    else:
        print('no')