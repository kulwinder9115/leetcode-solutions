# 1800: Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
class Solution(object):
    def maxAscendingSum(self, nums):
        current_sum=nums[0]
        max_sum=nums[0]
        for i in range (1,len(nums)):
            if nums[i-1]<nums[i]:
                current_sum= current_sum + nums[i]
            else:
                max_sum=max(max_sum,current_sum)
                current_sum= nums[i]
        max_sum=max(max_sum,current_sum)
        return max_sum

# Example usage:
solution = Solution()
nums = [10, 20, 30, 5, 10, 50]
print(solution.maxAscendingSum(nums))  # Output: 65