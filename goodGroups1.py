def construct(n, m, k):
    total = (n*(n+1)) // 2
    if k > total:
        return -1
    
    sequence = list(range(1, min(n ,m) + 1))
    
    while len(sequence) < n:
        sequence.append(sequence[-m])
        
    current_good = total    
    i = n - 1
    while current_good > k:
        max_reduce = i + 1
        if current_good - k >= max_reduce:
            sequence[i] = sequence[0]
            current_good -= max_reduce
        else:
            sequence[i] = sequence[0]
            current_good = k
            
        i -= 1
    
    return sequence


param = list(map(int, input().split()))
n = param[0]
m = param[1]
k = param[2]


result = construct(n, m, k)

print(result if result != -1 else -1)
