# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
#   "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <2: return len(s)
        left = 0
        res = 0
        dic = {}
        for i, val in enumerate(s):
            if val in dic:
                left = max(left, dic[val]+1)
            res = max(res, i - left + 1)
            dic[val] = i
        return res