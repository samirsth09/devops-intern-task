import sys

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./climbing_stairs.py <number_of_steps>")
        sys.exit(1)

    n = int(sys.argv[1])
    solution = Solution()
    print(solution.climbStairs(n))

