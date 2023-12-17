word = input().upper()
char_list = list(set(word))
cnt_list = [word.count(char) for char in char_list]
max_val = max(cnt_list)
max_cnt = cnt_list.count(max_val)
if max_cnt > 1:
    print('?')
else:
    maxIndex = cnt_list.index(max_val)
    char = char_list[maxIndex]
    print(char)