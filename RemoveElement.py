# 27. Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
class Solution(object):
    def removeElement(self, nums, val):
        p=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p]=nums[i]
                p=p+1
        return p
# Example usage:
nums = [3,2,2,3]
val = 3
obj= Solution()
length = obj.removeElement(nums, val)
print(length)  # Output: 2
print(nums[:length])  # Output: [2,2]
# Removes all instances of val in nums in-place and returns the new length.