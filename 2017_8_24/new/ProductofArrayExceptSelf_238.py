# Given an array of n integers where n > 1, nums,
#   return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
#
# Follow up:
# Could you solve it with constant space complexity?
#   (Note: The output array does not count as extra space for the purpose of space complexity analysis.)


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        m = 1
        z = 0
        for n in nums:
            if n != 0:
                m *= n
            else:
                z += 1
        if z:
            if z >= 2:
                return [0] * len(nums)
            else:
                return [0 if x != 0 else m for x in nums]
        else:
            return [m / x for x in nums]

    # def productExceptSelf(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     cur_product = 1
    #     n = len(nums)
    #     ans = [0]*n
    #     for i in xrange(n):
    #         ans[i] = cur_product
    #         cur_product = cur_product * nums[i]
    #     cur_product = 1
    #     for i in xrange(n-1, -1, -1):
    #         ans[i] = ans[i] * cur_product
    #         cur_product = cur_product * nums[i]
    #     return ans