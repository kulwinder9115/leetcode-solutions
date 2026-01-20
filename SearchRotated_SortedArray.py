# 33: Search in Rotated Sorted Array
class Solution(object):
    def search(self, nums, target):
        start=0
        end=len(nums)-1
        while start<=end:
            mid= start+end-start //2

            if nums[mid]==target:
                return mid
            elif nums[start]<=nums[mid]:
                if target>=nums[start] and target<nums[mid]:
                    end= mid-1
                else:
                    start=mid+1
            else:
                if target> nums[mid] and target <=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
        return -1
# Example usage:
sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))  # Output: 4d
            