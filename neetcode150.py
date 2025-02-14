class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchArray (self, nums: List[int], target_array: int) -> int:
            l = 0
            r = (len(nums) - 1)

            while l <= r:
                m = (l + r) // 2
                if (nums[m][0]) > target_array:
                    r = m - 1
                elif (nums[m][0]) < target_array:
                    l = m + 1
                elif (nums[m][-1]) > target_array and (nums[m][0]) < target_array:
                    left = 0
                    right = len((nums[m] - 1))

                    while left <= right:
                        mid = (left + right) // 2
                        if (nums[m][mid]) > target:
                            right = m-1
                        elif (nums[m][mid]) < target:
                            left = mid + 1
                        else:
                            return True
                    return False

                else:
                    return True
            return False
