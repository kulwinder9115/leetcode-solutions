# 2529 : Given a sorted array of integers nums, return the maximum between the count of positive integers and the count of negative integers.
class Solution(object):
    def maximumCount(self, nums):
        def NegativeInt(nums):
            start= 0 
            end= len(nums)-1
            ans=-1

            while start <= end:
                mid= start+(end-start)//2
                if nums[mid]<0:
                    ans=mid
                    start=mid+1
                else:
                    end=mid-1
            return ans
        def PositiveInt(nums):
            start = 0
            end= len(nums)-1
            ans= len(nums)
            while start <=end:
                mid=start+(end-start)//2
                if nums[mid]>0:
                    ans=mid
                    end=mid-1
                else:
                    start= mid+1
            return ans
        largestNegative= NegativeInt(nums)+1
        largestPositive= len(nums)-PositiveInt(nums)
        return max(largestNegative,largestPositive)
        
# Example usage:
sol = Solution()    
print(sol.maximumCount([-2,-1,-1,1,2,3]))  # Output: 3

