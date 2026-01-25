# 215 : Find the kth largest element in an array using a min-heap.
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        pq = []  # this will be our min-heap
        
        for num in nums:
            # Push the number into the heap
            heapq.heappush(pq, num)
            
            # If heap grows larger than k, remove the smallest
            if len(pq) > k:
                heapq.heappop(pq)
        
        # The root of the heap is the kth largest
        return pq[0]
# Example usage:
sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))  # Output: 5
