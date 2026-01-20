# 153: Find Minimum in Rotated Sorted Array II
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2

            if nums[mid] > nums[end]:
                # Minimum is in the right half
                start = mid + 1
            elif nums[mid] < nums[end]:
                # Minimum is in the left half (including mid)
                end = mid
            else:
                # nums[mid] == nums[end], shrink search space
                end -= 1

        return nums[start]
# Example usage:
sol = Solution()
print(sol.findMin([3,4,5,1,2]))  # Output: 1
