# 75: Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
# with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
class Solution(object):
    def sortColors(self, nums):
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                swap(nums, low, mid)
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                swap(nums, mid, high)
                high -= 1
# Example usage:
sol=Solution()
arr = [2, 0, 2, 1, 1, 0]
sol.sortColors(arr)
print(arr)  # Output: [0, 0, 1, 1, 2, 2]
