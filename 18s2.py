N = int(input())

sunflowers = []

for i in range(N):
    flower = list(map(int, input().split()))
    sunflowers.append(flower)
    
def is_ninety(a):
    for i in range(len(sunflowers[0]) - 1):
        for j in range(N):
            if sunflowers[i][j] >= sunflowers[i][j+1] and sunflowers[i][j] >=