# 1394: Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
# Return the largest lucky integer in the array. If there is no lucky integer return -1.
class Solution(object):
    def findLucky(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

    # Check lucky condition and track the largest
        ans = -1
        for num, count in freq.items():
            if num == count:
                ans = max(ans, num)

        return ans


# Example usage:
solution = Solution()
arr = [2, 2, 3, 4]
print(solution.findLucky(arr))  # Output: 2
