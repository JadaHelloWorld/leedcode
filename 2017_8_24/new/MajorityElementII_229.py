# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#   The algorithm should run in linear time and in O(1) space.
#


#todo
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # d = collections.Counter(nums)
        # m = d.most_common(2)
        # return [i for i, x in m if x >len(nums)/3]
        u_nums = list(set(nums))
        min_n = len(nums)/3
        res = []
        for n in u_nums:
            if nums.count(n) > min_n:
                res.append(n)
        return res