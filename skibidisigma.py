
n, m, r, c = map(int, input().split())
grid = [['a' for _ in range(m)] for _ in range(n)]

def isPalindrome(s):
    return s == s[::-1]

if r == 0 and c == 0 and n == 2 and m == 2:
    print("ab")
    print("ba")
    exit()

if r == 0 and c == 0 and n == 1 and m == 1:
    print("IMPOSSIBLE")
    exit()

if r == n and c != m and m % 2 == 1:
    if c % 2 == 0:
        start = c // 2 + 1
        en = c // 2 + 1 + m - c - 1
        for i in range(1, n):
            for j in range(start, en + 1):
                grid[i][j] = 'b'
    else:
        for i in range(1, n):
            start = 0
            total = 0
            adder = m - 1
            while total < m - c:
                grid[i][start] = 'b'
                grid[i][start + adder] = 'b'
                total += 2
                adder -= 2
                start += 1

    for i in range(n):
        print(''.join(grid[i]))
    exit()

if c == m and r != n and n % 2 == 1 and r != 0:
    if r % 2 == 0:
        start = r // 2 + 1
        en = r // 2 + 1 + n - r - 1
        for i in range(1, m):
            for j in range(start, en + 1):
                grid[j][i] = 'b'
    else:
        for i in range(1, m):
            grid[0][i] = 'b'
            grid[n - 1][i] = 'b'

    for i in range(n):
        print(''.join(grid[i]))
    exit()

if r == n and c != m and m % 2 == 0:
    if c % 2 == 1:
        print("IMPOSSIBLE")
        exit()
    else:
        for i in range(1, n):
            start = 0
            total = 0
            adder = m - 1
            while total < m - c:
                grid[i][start] = 'b'
                grid[i][start + adder] = 'b'
                total += 2
                adder -= 2
                start += 1

    for i in range(n):
        print(''.join(grid[i]))
    exit()

if c == m and r != n and n % 2 == 0 and r != 0:
    if r % 2 == 1:
        print("IMPOSSIBLE")
        exit()
    else:
        for i in range((r + 2) // 2, n - (r + 2) // 2 + 1):
            start = 1
            total = 0
            adder = n - 1
            while total < n - r:
                grid[i][start] = 'b'
                grid[i][start + adder] = 'b'
                total += 2
                adder -= 2
                start += 1

    for i in range(n):
        print(''.join(grid[i]))
    exit()

for i in range(r, n):
    grid[i][m - 1] = 'c'

for i in range(c, m):
    if grid[n - 1][i] == 'c':
        grid[n - 1][i] = 'd'
    else:
        grid[n - 1][i] = 'b'

rp = 0
for i in range(n):
    row = ''.join(grid[i])
    if isPalindrome(row):
        rp += 1

cp = 0
for i in range(m):
    col = ''.join([grid[j][i] for j in range(n)])
    if isPalindrome(col):
        cp += 1

if rp == r and cp == c:
    for i in range(n):
        print(''.join(grid[i]))
else:
    print("IMPOSSIBLE")