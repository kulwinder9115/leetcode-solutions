# Determine if a given integer is a power of two.
# Leetcode Problem 231: https://leetcode.com/problems/power-of-two/
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
# Example usage:
solution = Solution()
print(solution.isPowerOfTwo(1))  # True
print(solution.isPowerOfTwo(16)) # True
print(solution.isPowerOfTwo(3))  # False
