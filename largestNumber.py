# 179 : Given a list of non-negative integers nums, arrange them such that they form the largest number and return it as a string.
from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        # Convert numbers to strings
        nums = list(map(str, nums))
        
        # Custom comparator
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort using comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join sorted numbers
        result = ''.join(nums)
        
        # Handle case like [0,0]
        return '0' if result[0] == '0' else result
# Example usage:
sol = Solution()
print(sol.largestNumber([10,2]))          # Output: "210"
print(sol.largestNumber([3,30,34,5,9]))   # Output: "9534330"
