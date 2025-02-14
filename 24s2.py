T, N = map(int, input().split())

strings = []
res = []
for i in range(T):
    strings.append(input())
    
def is_alternating(string):
    count = {}
    for letter in string:
        count[letter] = 1 + count.get(letter, 0)
    for i in range(len(string)-1):
        if count[string[i]] > 1 and count[string[i + 1]] > 1:
            return False
        elif count[string[i]] == 1 and count[string[i+1]] == 1:
            return False
            
    return True
    
for i in strings:
    if is_alternating(i):
        res.append('T')
    else:
        res.append('F')
    
for i in res:
    print(i)