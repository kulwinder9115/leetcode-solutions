# LeetCode 268: Missing Number
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        actualSum = n * (n + 1) // 2
        currentSum=0
        for i in range(len(nums)):
            currentSum= currentSum+ nums[i]
        ans= actualSum- currentSum
        return ans
nums = [3, 0, 1]
solution = Solution()
print(solution.missingNumber(nums))  # Output: 2