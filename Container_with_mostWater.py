# 11:Container With Most Water
class Solution(object):
    def maxArea(self, height):
        max_capacity=0
        start=0
        end= len(height)-1
        while start< end:
            h=min(height[start],height[end])
            width= end- start
            current_capacity = h * width
            max_capacity= max(current_capacity,max_capacity)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return max_capacity


# Example usage:
solution = Solution()
heights = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(heights))  # Output: 49