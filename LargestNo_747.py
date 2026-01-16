# 747 Problem: In a given integer array nums, there is always exactly one largest element. 
# Find whether the largest element is at least twice as much as every other number in the array. If it is, return the index of the largest element,
# otherwise return -1.    

class Solution(object):
    def dominantIndex(self, nums):
        max=-1
        smax=-1
        maxidx=0
        for i in range(len(nums)):
            if max<nums[i]:
                smax=max
                max=nums[i]
                maxidx=i
            elif smax < nums[i]:
                smax=nums[i]
        if smax*2<=max:
            return maxidx
        else:
            return -1
# Example usage:
solution = Solution()
nums = [3, 6, 1, 0]
result = solution.dominantIndex(nums)
print(result)  # Output: 1
