# Given an array of integers nums sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
class Solution(object):
    def search(self, nums, target):
        low=0
        high= len(nums)-1
        while low <= high:
            mid= (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high= mid-1
            else:
                low=mid+1
        return -1
# Example usage:
sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))  # Output: 4




        