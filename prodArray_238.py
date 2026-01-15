# 238: Given an integer array 'nums', return an array 'answer' such that 'answer[i]' is equal to the product of all the elements of 'nums' except 'nums[i]'.
class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        right=[0]*n
        prod=1
        # Step 1: Build right product array
        right = [1] * n
        prod = 1
        for i in range(n-1, -1, -1):   # iterate backwards
            right[i] = prod
            prod *= nums[i]
        
        # Step 2: Build answer using left product
        ans = [0] * n
        left = 1
        for i in range(n):
            ans[i] = left * right[i]
            left *= nums[i]
        
        return ans
# Example usage:
solution = Solution()
nums = [1, 2, 3, 4]
result = solution.productExceptSelf(nums)
print(result)  # Output: [24, 12, 8, 6]
