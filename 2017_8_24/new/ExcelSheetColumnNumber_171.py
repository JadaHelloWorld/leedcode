# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # i = 1
        # res = []
        # while s:
        #     r = s%(26*i)
        #     s -= r
        #     res.append(chr(ord("A")+r))
        #     i += 1
        # return res[::-1]
        res = 0
        for i, n in enumerate(s[::-1]):
            res += (ord(n) - ord("A") + 1)*26**i
        return res