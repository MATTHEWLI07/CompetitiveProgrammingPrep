t = list(map(int, input().split()))

input_strings = []

for i in range(t[0]):
    input_line = input()
    input_strings.append([c for c in input_line])

#print(input_strings)

weight_lists = []

for i in range(t[0]):
    heavy_list = []
    for j in range(t[1]):
        is_heavy = (input_strings[i].count(input_strings[i][j]))
        if is_heavy == 1:
            heavy_list.append(1)
        else:
            heavy_list.append(2)
    weight_lists.append(heavy_list)


for i in range(len(weight_lists)):
    alternate = True
    for j in range(len(weight_lists[0]) - 1):
        if weight_lists[i][j] == weight_lists[i][j+1]:
            alternate = False

    if alternate:
        print('T')
    else:
        print('F')




