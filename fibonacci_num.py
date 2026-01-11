class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1

        first_term = 0
        second_term = 1

        for i in range(2, n + 1):
            third_term = first_term + second_term
            first_term = second_term
            second_term = third_term

        return second_term

# Test the function
if __name__ == "__main__":
    sol = Solution()
    for i in range(10):
        print(f"fib({i}) = {sol.fib(i)}")