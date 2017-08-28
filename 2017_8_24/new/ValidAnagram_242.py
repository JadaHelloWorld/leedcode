# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chars = set(s)
        if chars != set(t):
            return False
        for c in chars:
            if s.count(c) != t.count(c):
                return False
        return True