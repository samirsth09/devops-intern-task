import sys


class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 step and 2 steps
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Dynamic programming array to store results
        dp = [0] * (n + 1)
        # The number of ways to climb 1 step is 1
        dp[1] = 1
        # The number of ways to climb 2 steps is 2
        dp[2] = 2

        # Iteratively calculate the number of ways for each step
        for i in range(3, n + 1):
            # The number of ways to reach step 'i' is the sum of ways to reach steps (i-1) and (i-2)
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]  # Return the number of ways to climb 'n' steps


# Main function to parse command-line argument and execute the solution
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./climbing_stairs.py <number_of_steps>")
        sys.exit(1)

    n = int(sys.argv[1])  # Parse the number of steps from the command-line argument
    solution = Solution()  # Create an instance of the Solution class
    print(solution.climbStairs(n))  # Print the result of climbing 'n' steps


