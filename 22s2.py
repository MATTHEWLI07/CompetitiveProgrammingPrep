x = int(input())

tgthr = [list(map(str, (input().split()))) for _ in range(x)]

apart = [list(map(str, (input().split()))) for _ in range(x)]

g = int(input())
groups = [list(map(str, input().split())) for _ in range(g)]

print(tgthr)
print(apart)
print(groups)
res = 0

for group in groups:
    for pair in apart:
        if pair[0] in group and pair[1] in group:
            res += 1

    for pair in tgthr:
        if pair[0] in group and pair[1] not in group:
            res += 1
print(res)