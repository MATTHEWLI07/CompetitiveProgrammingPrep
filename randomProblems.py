grid = []

m = int(input())
n = int(input())
for i in range(m):
    grid.append([0] * n)

k = int(input())
choices = []

for i in range(k):
    choices.append(list(input().split()))
    
for i in choices:
    if i[0] == 'R':
        row_num = int(i[1]) - 1
        if 0 <= row_num < m:
            for _ in range(n):
                grid[row_num][_] = 1 - grid[row_num][_]
    
    else:
        column = int(i[1]) - 1
        if 0<= column < n:
            for j in range(m):
                grid[j][column] = 1 - grid[j][column]

count = 0
for row in range(m):
    for col in range(n):
        if grid[row][col] == 1:
            count += 1
            
print(count)
    
    
    