org = list(map(int, input().split()))

target = list(map(int, input().split()))

def find_different_ranges(arr1, arr2):
    diff= []
    start = None

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            if start is None:
                start = i
        else:
            if start is not None:
                diff.append[[start, i - 1]]
                start = None

    if start is not None:
        diff.append([start, len(arr1) - 1])

    return diff

indices = find_different_ranges(org, target)

