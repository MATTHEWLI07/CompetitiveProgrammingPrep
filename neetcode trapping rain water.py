def trap(heights):
    n = len(heights)
    if n < 3:
        return 0

    total_water = 0
    left = 0

    while left < n - 1:
        right = left + 1

        if heights[left] > heights[right]:
            check = right + 1
            found_boundary = False

            while check < n:
                if heights[check] >= heights[left]:
                    found_boundary = True
                    break
                check += 1

            if found_boundary:
                for i in range(right, check):
                    total_water += heights[left] - heights[i]
                left = check
            else:
                left += 1
        else:
            left += 1

    return total_water


height = list(int(c) for c in input() if c.isalnum())
print(trap(height))

