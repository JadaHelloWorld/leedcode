# Given an array of integers,
#   find out whether there are two distinct indices i and j in the array
#   such that the absolute difference between nums[i] and nums[j] is at most t
#   and the absolute difference between i and j is at most k.


#todo
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        d = {}  # collections.OrderedDict()
        w = t + 1
        for i, n in enumerate(nums):
            new_n = n / w
            for x in [new_n, new_n - 1, new_n + 1]:
                if x in d and abs(d[x] - n) <= t:
                    return True
            d[new_n] = n
            if i >= k:
                del d[nums[i - k] / w]
                # d.popitem(last=False)

        return False


if __name__ == "__main__":
    s = Solution()
    res = s.containsNearbyAlmostDuplicate([2,1], 1,1)
    print res