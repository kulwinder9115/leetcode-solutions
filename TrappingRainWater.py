# 42 : Trapping Rain Water Problem
class Solution(object):
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0

        leftMax = [0] * n
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])

        rightMax = [0] * n
        rightMax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        ans = 0
        for i in range(n):
            ans += min(leftMax[i], rightMax[i]) - height[i]

        return ans
# Example usage:
sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
