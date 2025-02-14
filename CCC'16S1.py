#strat is to compare

def is_wildcard_anagram(s1, s2):
    from collections import Counter

    count_s1 = Counter(s1)

    for char in s2:
        if char != '*':
            if char in count_s1 and count_s1[char] > 0:
                count_s1[char] -= 1
            else:
                return 'N'

    return 'A'


s1 = input().strip()
s2 = input().strip()

print(is_wildcard_anagram(s1, s2))
