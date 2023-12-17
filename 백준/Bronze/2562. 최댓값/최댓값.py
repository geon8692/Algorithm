values = []
for _ in range(9):
    values.append(int(input()))
max_value = max(values)
max_index = values.index(max_value)
print(max_value)
print(max_index+1)