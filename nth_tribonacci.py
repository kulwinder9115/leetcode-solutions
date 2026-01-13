# Calculate the n-th Tribonacci number.
# Leetcode Problem 1137: https://leetcode.com/problems/n-th-tribonacci-number
class Solution(object):
    def tribonacci(self, n):
        if n==0 :
            return 0
        elif n==1 or n==2:
            return 1
        else :
            fir_term=0
            sec_term=1
            thir_term=1
            for i in range(n):
                for_term= fir_term + sec_term + thir_term
                fir_term=sec_term
                sec_term=thir_term
                thir_term = for_term
            return fir_term
# Example usage:
solution = Solution()
print(solution.tribonacci(4))  # 4
print(solution.tribonacci(25)) # 1389537
print(solution.tribonacci(0))  # 0