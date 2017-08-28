# Given two words (beginWord and endWord), and a dictionary's word list,
#   find all shortest transformation sequence(s) from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a set of strings).
#   Please reload the code definition to get the latest changes.

import collections


#todo
class Solution(object):
    #     def findLadders(self, beginWord, endWord, wordList):
    #         """
    #         :type beginWord: str
    #         :type endWord: str
    #         :type wordList: List[str]
    #         :rtype: List[List[str]]
    #         """
    #         wordSet = set(wordList)
    #         if endWord not in wordSet:
    #             return []

    #         start = [(beginWord,[beginWord])]
    #         # min_l = 1
    #         res = []
    #         n = set()
    #         size = len(beginWord)
    #         for w in wordSet:
    #             for i in range(size):
    #                 n.add(w[:i] + "_" + w[i+1:])
    #         while start and not res:
    #             level = []
    #             for cur, path in start:
    #                 if cur == endWord and path not in res:
    #                     res.append(path)
    #                 for i in range(len(beginWord)):
    #                     left, right = cur[:i], cur[i+1:]
    #                     if left + "_" + right in n:
    #                         for j in "abcdefghigklmnopqrstuvwxyz":

    #                             new = left + j + right
    #                             if new in wordSet:
    #                                 # wordSet.remove(new)
    #                                 level.append((new, path + [new]))
    #             # min_l += 1
    #             start = level
    #         return res
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        word_set = set(wordlist)
        if endWord not in word_set: return []

        front_level = {beginWord}
        path_dic = collections.defaultdict(list)

        while front_level:
            if len(front_level) == 0:
                return False
            for word in (front_level):
                word_set.discard(word)
            next_level = set()
            done = False

            for word in front_level:
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(word)):
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word == endWord:
                            done = True
                            path_dic[word].append(new_word)
                        else:
                            if new_word in word_set:
                                next_level.add(new_word)
                                path_dic[word].append(new_word)
            if done:
                break
            front_level = next_level
        path, paths = [beginWord], []

        def construct_path(word, path):
            if word == endWord:
                paths.append(path)
                return
            if word in path_dic:
                for item in path_dic[word]:
                    construct_path(item, path + [item])

        construct_path(beginWord, path)
        return paths
