N = int(input())
to_process = []

for i in range(N):
    to_process.append(int(input()))

res = 0

for i in range(N // 2):
    if to_process[i] == to_process[i + N // 2]:
        res += 1
        
print(res)

