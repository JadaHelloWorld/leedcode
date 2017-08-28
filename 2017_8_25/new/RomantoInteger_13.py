# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I":1, "V":5, "X":10, "L":50,"C":100, "D":500,"M":1000}
        z = 0
        for i, n in enumerate(s[:-1]):
            if d[n] < d[s[i+1]]:
                z -= d[n]
            else:
                z += d[n]
        return z + d[s[-1]]