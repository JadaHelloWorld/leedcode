# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # dic = {}
        # for i in strs:
        #     counter = str(sorted(collections.Counter(i).items()))
        #     if counter in dic:
        #         dic[counter].append(i)
        #     else:
        #         dic[counter] = [i]
        # return [v for k,v in dic.iteritems()]
        if not strs: return []
        dic = dict()
        for s in strs:
            l_s = str(sorted(list(s)))
            if l_s not in dic:
                dic[l_s] = [s]
            else:
                dic[l_s].append(s)
        return dic.values()
