# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares
class Solution(object):
    def sortedSquares(self, nums):
          ans= [0]* len(nums)
          start =0
          end= len(nums)-1
          ptr= len(ans)-1 
          while start <= end :
            ss= nums[start]*nums[start]
            es= nums[end]*nums[end]
            if ss > es:
                ans[ptr]= ss
                start=start+1
            else:
                ans[ptr]=es
                end = end-1
            ptr=ptr-1
          return ans
# of each number sorted in non-decreasing order.
nums = [-4,-1,0,3,10]
obj= Solution()
print(obj.sortedSquares(nums))  # Output: [0,1,9,16,100]


    