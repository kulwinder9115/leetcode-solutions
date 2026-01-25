# 66 : Plus One
class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        # Traverse from the last digit backwards
        for i in range(n-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                # Set all digits after i to 0
                for j in range(i+1, n):
                    digits[j] = 0
                return digits
            # If digit is 9, set it to 0 and continue loop
            digits[i] = 0
        
        # If all digits were 9, we need an extra digit
        return [1] + [0] * n
# Example usage:
sol = Solution()
print(sol.plusOne([1,2,3]))  # Output: [1,2,4]
print(sol.plusOne([9,9,9]))  # Output: [1,0,0,0]