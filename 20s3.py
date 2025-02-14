from collections import Counter

def count_distinct_permutations(needle, haystack):
    len_n = len(needle)
    len_h = len(haystack)
    
    if len_n > len_h:
        return 0
    
    def compute_hash(counter):
        return tuple(sorted(counter.items()))

    needle_counter = Counter(needle)
    needle_hash = compute_hash(needle_counter)

    window_counter = Counter(haystack[:len_n])
    window_hashes = set()
    
    if compute_hash(window_counter) == needle_hash:
        window_hashes.add(tuple(haystack[:len_n]))
    
    for i in range(1, len_h - len_n + 1):
        outgoing_char = haystack[i - 1]
        incoming_char = haystack[i + len_n - 1]
        
        window_counter[outgoing_char] -= 1
        if window_counter[outgoing_char] == 0:
            del window_counter[outgoing_char]
        window_counter[incoming_char] += 1
        
        if compute_hash(window_counter) == needle_hash:
            current_window = tuple(haystack[i:i + len_n])
            window_hashes.add(current_window)
    
    return len(window_hashes)

N = int(input())
H = int(input())
print(count_distinct_permutations(N, H))
