#53: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
class Solution(object):
    def maxSubArray(self, nums):
        currsum=nums[0]
        maxsum=nums[0]
        for i in range(1,len(nums)):
            if currsum+nums[i] >nums[i]:
                currsum+= nums[i]
            else:
                currsum=nums[i]
            maxsum=max(maxsum,currsum)
        return maxsum
# Example usage:
sol=Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
