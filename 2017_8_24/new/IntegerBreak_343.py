# Given a positive integer n, break it into the sum of at least two positive integers
#   and maximize the product of those integers. Return the maximum product you can get.
#
# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
#
# Note: You may assume that n is not less than 2 and not larger than 58.


# todo

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        return max([self.mulSplitInt(n, x) for x in range(2, n + 1)])

    def mulSplitInt(self, n, m):
        unit = n / m
        remainder = n % m
        return (unit + 1) ** remainder * (unit) ** (m - remainder)
    #
    # def integerBreak(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n <= 3: return n - 1
    #     dp = [0] * (n + 1)
    #     dp[2], dp[3] = 2, 3
    #     for x in range(4, n + 1):
    #         dp[x] = max(3 * dp[x - 3], 2 * dp[x - 2])
    #     return dp[n]