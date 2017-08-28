# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
# Example:
#
# Input: "cbbd"
#
# Output: "bb"


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 0:
            return
        maxLen = 1
        start = 0
        for i in xrange(len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2

            elif i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start:start + maxLen]

    # def getlongestpalindrome(self, s, l, r):
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         l -= 1;
    #         r += 1
    #     return s[l + 1: r]
    #
    # def longestPalindrome(self, s):
    #     palindrome = ''
    #     for i in range(len(s)):
    #         len1 = len(self.getlongestpalindrome(s, i, i))
    #         if len1 > len(palindrome): palindrome = self.getlongestpalindrome(s, i, i)
    #         len2 = len(self.getlongestpalindrome(s, i, i + 1))
    #         if len2 > len(palindrome): palindrome = self.getlongestpalindrome(s, i, i + 1)
    #     return palindrome