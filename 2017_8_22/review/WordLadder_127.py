# Given two words (beginWord and endWord), and a dictionary's word list,
#   find the length of shortest transformation sequence from beginWord to endWord,
#   such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a set of strings).
#   Please reload the code definition to get the latest changes.
#


class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        wordSet = set(wordDict)
        if endWord not in wordSet:
            return 0
        size = len(beginWord)
        stack = [(beginWord, 1)]
        while stack:
            cur, l = stack.pop(0)
            if cur == endWord:
                return l
            for i in range(size):
                left = cur[:i]
                right = cur[i + 1:]
                for j in "abcdefghigklmnopqrstuvwxyz":
                    if cur[i] != j:
                        new = left + j + right
                        if new in wordSet:
                            wordSet.remove(new)
                            stack.append((new, l+1))
        return 0