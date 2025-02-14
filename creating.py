n, m, r, c = [int(i) for i in input().split()]

result = [['a' for _ in range(n)] for _ in range(m)]

if r > n or c > m or r + c > n + m - 1:
    print("IMPOSSIBLE")

for i in range(n - r):
    result[i][0] = 'b'
    
for j in range(m - c):
    result[0][j] = 'b'
    
if n - r > 0 and m - c > 0:
    result[0][0] = 'a'
    
for row in result:
    print(''.join(row))
