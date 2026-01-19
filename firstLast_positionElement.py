# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
class Solution(object):
    def searchRange(self, nums, target):
        def firstOccurrence(nums, target):
            start, end = 0, len(nums) - 1
            ans = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    ans = mid
                    end = mid - 1   # keep searching left
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return ans

        def lastOccurrence(nums, target):
            start, end = 0, len(nums) - 1
            ans = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    ans = mid
                    start = mid + 1   # keep searching right
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return ans

        return [firstOccurrence(nums, target), lastOccurrence(nums, target)]
    
# Example usage:
sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))  # Output: [3, 4]

                



        