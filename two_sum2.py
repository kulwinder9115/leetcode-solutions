# 167:Given a 1-indexed array of integers 'numbers' that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.    

class Solution(object):
    def twoSum(self, numbers, target):
        ans=[0]*2
        start=0
        end= len(numbers)-1
        while start< end:
            sum = numbers[start]+ numbers[end]
            if sum==target:
                ans[0]=start+1
                ans[1]=end+1
                return ans
            elif sum> target :
                end = end-1
            else: 
                start=start+1
        return ans



# Example usage:
solution = Solution()
numbers = [2, 7, 11, 15]
target = 9
result = solution.twoSum(numbers, target)
print(result)  # Output: [1, 2]
