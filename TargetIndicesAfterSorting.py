# 205 : Target Indices After Sorting Array
class Solution(object):
    def targetIndices(self, nums, target):
        num = 0
        targetCount = 0
        
        # Count numbers less than target and equal to target
        for ele in nums:
            if ele == target:
                targetCount += 1
            elif ele < target:
                num += 1
        
        # Build the answer list
        ans = []
        while targetCount > 0:
            ans.append(num)
            num += 1
            targetCount -= 1
        
        return ans
# Example usage:
sol = Solution()
print(sol.targetIndices([1,2,5,2,3], 2))  # Output: [1, 2]
print(sol.targetIndices([1,2,5,2,3], 3))  # Output: [4]