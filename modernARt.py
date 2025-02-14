M = int(input())
N = int(input())
K = int(input())

row_toggles = [0] * M
col_toggles = [0] * N

for _ in range(K):
    rc, which = input().split()
    which = int(which) - 1
    if rc == 'R':
        row_toggles[which] ^= 1
    elif rc == 'C':
        col_toggles[which] ^= 1

rows_toggled = sum(row_toggles)
cols_toggled = sum(col_toggles)

gold = (rows_toggled * N) + (cols_toggled * M) - (2 * rows_toggled * cols_toggled)
print(gold)