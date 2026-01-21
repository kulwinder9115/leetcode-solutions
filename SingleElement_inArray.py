# 540: You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. 
# Find this single element that appears only once.  
class Solution(object):
    def singleNonDuplicate(self, nums):
        if len(nums)==1:
            return nums[0]
        elif nums[0]!=nums[1]:
            return nums[0]
        elif nums[len(nums)-1]!=nums[len(nums)-2]:
            return nums[len(nums)-1]
        start=0
        end=len(nums)-1
        while start<=end:
            mid=start+(end-start)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
                #vmid index odd
            elif mid % 2==1 : 
                if nums[mid-1]==nums[mid]:
                    start=mid+1
                else:
                    end= mid-1
                # mid even index
            else :
                if nums[mid]==nums[mid+1]:
                    start= mid+1
                else:
                    end= mid-1
        return -1



# Example usage:
sol=Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))  # Output: 2
print(sol.singleNonDuplicate([3,3,7,7,10,11,11]))  # Output: 10