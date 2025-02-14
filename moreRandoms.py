n = int(input())

grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
    
def mult_90(matrix):
    return [list(row) for row in zip(*matrix)][::-1]
        
def mult_180(matrix):
    return [row[::-1] for row in matrix[::-1]]
    
def mult_270(matrix):
    return [list(row)[::-1] for row in zip(*matrix)]


def is_rotated_90(matrix):

    for col in range(n):
        for row in range(n - 1):
            if matrix[row][col] >= matrix[row + 1][col]:
                return False

    for row in matrix:
        if not all(row[i] > row[i + 1] for i in range(len(row) - 1)):
            return False

    return True

def is_rotated_180(matrix):
    for row in range(n - 1):
        if matrix[row] <= matrix[row + 1]:
            return False

    for row in matrix:
        if not all(row[i] > row[i + 1] for i in range(len(row) - 1)):
            return False

    return True

def is_rotated_270(matrix):
    for col in range(n):
        for row in range(n - 1):
            if matrix[row][col] <= matrix[row + 1][col]:
                return False

    for row in matrix:
        if not all(row[i] < row[i + 1] for i in range(len(row) - 1)):
            return False

    return True

def is_rotated_360(matrix):
    for col in range(n):
        for row in range(n - 1):
            if matrix[row][col] >= matrix[row+1][col]:
                return False
            
    for row in matrix:
        if not all(row[i] < row[i+1] for i in range(len(row) - 1)):
            return False
        
    return True


if is_rotated_90:
    res = mult_90(grid)
elif is_rotated_180:
    res = mult_180(grid)
elif is_rotated_270:
    res = mult_270(grid)
elif is_rotated_360:
    res = grid
    
print(res)