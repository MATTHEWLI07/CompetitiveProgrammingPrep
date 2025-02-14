N = int(input())
swifts = list(map(int, input().split()))
semaphores = list(map(int, input().split()))


def countRuns(N, swifts, semaphores):
    swiftRuns = 0
    semaphoreRuns = 0
    k = 0
    for day in range(1, N + 1):
        swiftRuns += swifts[day-1]
        semaphoreRuns += semaphores[day-1]

        if swiftRuns == semaphoreRuns:
            k = day
    return k


print(countRuns(N, swifts, semaphores))