s = input()

def isPalindrome(s):
    string = list(c.lower() for c in s if c.isalpha())
    pal_count = 0
    left = 0
    stringlength = len(string)
    right = len(string) - 1
    while left <= right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

print(isPalindrome(s))