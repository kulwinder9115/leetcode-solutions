# 162: A peak element is an element that is strictly greater than its neighbors. 
# Given an integer array nums, find a peak element, and return its index. 
# If the array contains multiple peaks, return the index to any of the peaks.
class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)
        if n==1:
            return 0
        elif nums[0]>nums[1]:
            return 0
        elif nums[n-1]>nums[n-2]:
            return n-1
        start=1
        end=n-2
        while start<=end:
            mid=start+(end-start)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]<nums[mid+1]:
                start=mid+1
            else:
                end=mid-1
        return -1
# Example usage:
sol=Solution()
print(sol.findPeakElement([1,2,3,1]))  # Output: 2
print(sol.findPeakElement([1,2,1,3,5,6,4]))  # Output: 5
            

        