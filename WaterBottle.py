class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        ans = numBottles
        while (numBottles>=numExchange ):
            newBottles = numBottles// numExchange
            remBottles = numBottles % numExchange
            ans= ans + newBottles
            numBottles = newBottles+ remBottles
        return ans
    

# Example usage:
numBottles = 9  
numExchange = 3
solution = Solution()
print(solution.numWaterBottles(numBottles, numExchange))  # Output: 13