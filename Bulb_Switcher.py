# 319 Problem: Given n bulbs that are initially off, you toggle the state of the bulbs in a specific pattern. 
# After n rounds of toggling, return the number of bulbs that are on.
class Solution(object):
    def bulbSwitch(self, n):
        count=0
        i=1
        while i*i<=n:
            count+=1
            i+=1
        return count
# Example usage:
solution = Solution()
n = 10
result = solution.bulbSwitch(n)
print(result)  # Output: 3