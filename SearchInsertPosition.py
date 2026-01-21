# 35: Given a sorted array of distinct integers and a target value, return the index if the target is found.
#  If not, return the index where it would be if it were inserted in order.
class Solution(object):
    def searchInsert(self, nums, target):
        start=0
        end=len(nums)-1
        while start<=end:
            mid=start+(end-start)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end=mid-1
            else:
                start=mid+1
        return start

# Example usage:
sol=Solution()
print(sol.searchInsert([1,3,5,6],5))  # Output: 2
print(sol.searchInsert([1,3,5,6],2))  # Output: 1