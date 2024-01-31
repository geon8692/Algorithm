N, r, c = map(int, input().split())

result = 0

def divide(x, y, length):
    global result

    if x == r and y == c:
        print(result)
    elif length == 1:
        result += 1
    elif not (x <= r < x+length and y <= c < y+length):
        result += length * length
    else:
        divide(x, y, length//2)
        divide(x, y + length//2, length//2)
        divide(x + length//2, y, length//2)
        divide(x + length//2, y + length//2, length//2)

divide(0, 0, 2**N)