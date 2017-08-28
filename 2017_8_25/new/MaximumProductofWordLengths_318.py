# Given a string array words, find the maximum value of length(word[i]) * length(word[j])
#   where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
#
# Example 1:
# Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# Return 16
# The two words can be "abcw", "xtfn".
#
# Example 2:
# Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# Return 4
# The two words can be "ab", "cd".
#
# Example 3:
# Given ["a", "aa", "aaa", "aaaa"]
# Return 0
# No such pair of words.


#todo
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 1
        ord_a = ord("a")
        d = {}
        for word in words:
            mark = 0
            for w in set(word):
                mark |= 1 << (ord(w) - ord_a)
            if mark in d:
                d[mark] = max(len(word), d[mark])
            else:
                d[mark] = len(word)
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
