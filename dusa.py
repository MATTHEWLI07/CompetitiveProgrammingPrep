t, n = [int(i) for i in input().split()]

strings = []

for i in range(t):
    strings.append(str(input()))

def heavy_light(a):
    string = {}
    for i in a:
        string[i] = 1 + string.get(i, 0)
    return string

def check_heavy_light(menga, b):
    prev = ''
    menga[prev] = 0
    for i in b:
        if menga[i] > 1 and menga[prev] > 1:
            return False
        elif menga[i] == 1 and menga[prev] == 1:
            return False
        prev = i
    return True


for i in strings:
    menga = heavy_light(i)
    if check_heavy_light(menga, i):
        print('T')
    else:
        print('F')