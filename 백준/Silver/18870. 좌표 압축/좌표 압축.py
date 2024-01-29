N = int(input())
input_list = list(map(int, input().split()))

sorted_list = sorted(set(input_list))

dict_list = dict(zip(sorted_list, list(range(len(sorted_list)))))

for x in input_list:
    print(dict_list[x], end=' ')