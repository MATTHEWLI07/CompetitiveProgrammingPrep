n = list(map(int, input().split()))

inputs = []

for i in range(n[0]):
    sigma = input()
    inputs.append([c for c in sigma])

heavies = []    
    

for i in range(n[0]):
    heavy_list = []
    for j in range(n[1]):
        is_heavy = (inputs[i].count(inputs[i][j]))
        if is_heavy == 1:
            heavy_list.append(1)
        else:
            heavy_list.append(2)
    heavies.append(heavy_list)

for i in range(len(heavies)):
    valid = True
    for j in range(len(heavies[0]) - 1):
        if heavies[i][j] == heavies[i][j+1]:
            valid = False
        
    if valid:
        print('T')
    else:
        print('F')