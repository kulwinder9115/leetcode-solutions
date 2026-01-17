# 334: Increasing Triplet Subsequence
class Solution(object):
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')
        third = float('inf')

        for i in range(len(nums)):
            element= nums[i]
            if first >= element:
                first= element
            elif second >= element:
                second= element
            else:
                third= element
                return True
        return False  
# Example usage:
solution = Solution()
nums = [1, 2, 3, 4, 5]
print(solution.increasingTriplet(nums))  # Output: True
