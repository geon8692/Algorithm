while True:
    sides = list(map(int, input().split()))
    if sides == [0, 0, 0]:
        break
    large_value = sides.pop(sides.index(max(sides)))
    if sides[0]**2 + sides[1]**2 == large_value**2:
        print('right')
    else:
        print('wrong')