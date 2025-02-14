n = int(input())

villages = [int(input()) for _ in range(n)]

villages.sort()

min_size = float('inf')

for i in range(1, len(villages) - 1):
    left_mid = (villages[i] + villages[i - 1]) / 2
    right_mid = (villages[i + 1] + villages[i]) / 2
    neighborhood_size = right_mid - left_mid
    min_size = min(min_size, neighborhood_size)

print(f"{min_size:.1f}")
