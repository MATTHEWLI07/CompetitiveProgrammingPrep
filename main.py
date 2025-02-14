'''

N = int(input())
H = [int(input()) for _ in range(N)]


count = 0

for i in range(N):
    if H[i] == H[(i + N//2) % N]:
        count += 1
r
print(count)

from collections import Counter


def getHeavyLightLetters(string):
    letterCounts = Counter(string)
    heavyLetters = set()
    lightLetters = set()

    for char, count in letterCounts.items():
        if count > 1:
            heavyLetters.add(char)
        else:
            lightLetters.add(char)

    return heavyLetters, lightLetters


def isAlternating(string, heavyLetters, lightLetters):
    isHeavy = string[0] in heavyLetters

    for i in range(1, len(string)):
        currentChar = string[i]
        currentIsHeavy = currentChar in heavyLetters

        if currentIsHeavy == isHeavy:
            return False

        isHeavy = not isHeavy

    return True


T, N = map(int, input().split())
strings = [input().strip() for _ in range(T)]

results = []
for string in strings:
    heavyLetters, lightLetters = getHeavyLightLetters(string)
    if isAlternating(string, heavyLetters, lightLetters):
        results.append("T")
    else:
        results.append("F")

for result in results:
    print(result)

C = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

road = [row1, row2]


def calculatePerimeter(road):
    totalTape = 0

    def oneRow(row):
        tape = 0
        n = len(row)
        for i in range(n):
            if row[i] == 1:
                # For a single tile, initially assume it has 3 sides
                tape += 3
                # Check if the previous tile is also wet (shares one side)
                if i > 0 and row[i - 1] == 1:
                    tape -= 2  # One side is shared with the previous tile
        return tape

    # Calculate perimeter for the first row
    totalTape += oneRow(road[0])

    # Calculate perimeter for the second row
    totalTape += oneRow(road[1])

    # Adjust for shared sides between the two rows (only on odd-numbered columns)
    for i in range (C):
        if road[0][i] == 1 and road[1][i] == 1 and i % 2 == 1:
            totalTape -= 2  # Subtract shared side for each pair of adjacent wet tiles

    return totalTape


print(calculatePerimeter(road))


def findMostSymmetricCrop(N, heights):
    result = []

    for length in range(1, N + 1):
        minAsymmetricValue = float('inf')

        for mid in range(N):
            asymmetricValue = 0
            start = mid - (length - 1) // 2
            end = mid + length // 2

            if start < 0 or end >= N:
                continue

            for i in range((length // 2) + 1):
                left = heights[start - i]
                right = heights[end + i]
                asymmetricValue += abs(left - right)

            if asymmetricValue < minAsymmetricValue:
                minAsymmetricValue = asymmetricValue

        result.append(minAsymmetricValue)

    return result


data = input().split()
N = int(data[0])
heights = list(map(int, data[1:]))

result = findMostSymmetricCrop(N, heights)
print(' '.join(map(str, result)))



def foursAndFives(N):
    count = 0
    for i in range(N // 5+1):
        remainder = N - i * 5
        if remainder % 4 == 0:
            count +=1
    return count

N = int(input())
print (foursAndFives(N))



def countViolations():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    index = 0

    x = int(data[index])
    index += 1
    togetherConstraints = set()
    for _ in range(x):
        pair = tuple(data[index].split())
        togetherConstraints.add(pair)
        index += 1

    y = int(data[index])
    index += 1
    separateConstraints = set()
    for _ in range(y):
        pair = tuple(data[index].split())
        separateConstraints.add(pair)
        index += 1

    g = int(data[index])
    index += 1
    groups = []
    for _ in range(g):
        group = data[index].split()
        groups.append(set(group))
        index += 1

    violations = 0

    for group in groups:
        groupList = list(group)
        for i in range(3):
            for j in range(i + 1, 3):
                pair = (groupList[i], groupList[j])
                if pair in togetherConstraints or (pair[1], pair[0]) in togetherConstraints:
                    togetherConstraints.remove(pair if pair in togetherConstraints else (pair[1], pair[0]))
                if pair in separateConstraints or (pair[1], pair[0]) in separateConstraints:
                    violations += 1

    for constraint in togetherConstraints:
        found = False
        for group in groups:
            if constraint[0] in group and constraint[1] in group:
                found = True
                break
        if not found:
            violations += 1

    print(violations)

import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
heights = list(map(int, data[1:n + 2]))
widths = list(map(int, data[n + 2:n + 2 + n]))

totalArea = 0
for i in range(n):
    leftHeight = heights[i]
    rightHeight = heights[i + 1]
    width = widths[i]
    area = (leftHeight + rightHeight) * width / 2
    totalArea += area

print(totalArea)




m = int(input())
n = int(input())
k = int(input())

rowToggles = [0] * m
colToggles = [0] * n

index = 3
for _ in range(k):
    operation, number = input().split()
    number = int(number) - 1
    if operation == 'R':
        rowToggles[number] += 1
    elif operation == 'C':
        colToggles[number] += 1
    index += 2

oddRowToggles = sum(1 for x in rowToggles if x % 2 == 1)
oddColToggles = sum(1 for x in colToggles if x % 2 == 1)
goldCells = (oddRowToggles * (n - oddColToggles)) + ((m - oddRowToggles) * oddColToggles)
print(goldCells)



import sys


def mostSymmetricCrop(N, heights):
    result = [0]
    preVal = [[0] * (N + 1) for _ in range(N + 1)]

    for length in range(2, N + 1):
        minAsymmetricVal = float('inf')
        left = 0
        right = length - 1

        while right < N:
            preVal[left][right] = abs(heights[left] - heights[right]) + (
                preVal[left + 1][right - 1] if left + 1 <= right - 1 else 0)
            if preVal[left][right] < minAsymmetricVal:
                minAsymmetricVal = preVal[left][right]
            left += 1
            right += 1

        result.append(minAsymmetricVal)

    return result



input = sys.stdin.read
data = input().split()
N = int(data[0])
heights = list(map(int, data[1:]))


result = mostSymmetricCrop(N, heights)
print(result)

def calculateMaxSpeed(observations):
    observations.sort()
    maxSpeed = 0
    for i in range(len(observations) - 1):
        T1, X1 = observations[i]
        T2, X2 = observations[i + 1]
        speed = abs(X2 - X1) / (T2 - T1)
        maxSpeed = max(maxSpeed, speed)
    return maxSpeed

N = int(input())
observations = []
for _ in range(N):
    T, X = map(int, input().split())
    observations.append((T, X))

maxSpeed = calculateMaxSpeed(observations)
print(f"{maxSpeed:.2f}")



instruct = input()
grid = [[1, 2], [3, 4]]

for i in instruct:
    if i == 'H':
        grid[0], grid[1] = grid[1], grid[0]
    else:
        grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
        grid[1][0], grid[1][1] = grid[1][1], grid[1][0]

for row in grid:
    print(' '.join(map(str, row)))




villages = int(input())
numLine = []
for _ in range(villages):
    numLine.append(int(input()))

numLine.sort()
neighborhood = []

for i in range(1, villages - 1):
    leftMid= (numLine[i] + numLine[i - 1]) / 2
    rightMid = (numLine[i] + numLine[i + 1]) / 2
    nSize = rightMid - leftMid
    neighborhood.append(nSize)

minN = min(neighborhood)

print(f"{minN:.1f}")

'''