# LeetCode 1464: Maximum Product of Two Elements in an Array

class max_prod_two_arrayElements(object):
    def maxProduct(self, nums):
        smax = -1
        max_val = -1
        
        for i in range(len(nums)):
            if max_val < nums[i]:
                smax = max_val
                max_val = nums[i]
            elif smax < nums[i]:
                smax = nums[i]
        
        ans = (max_val - 1) * (smax - 1)
        return ans


# Example usage:
nums = [3, 4, 5, 2]
solution = max_prod_two_arrayElements()
print(solution.maxProduct(nums))  # Output: 12