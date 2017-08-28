# Given an array of size n, find the majority element.
##  The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums_d = collections.Counter(nums)
        # return nums_d.most_common(1)[0][0]
        nums.sort()
        return nums[len(nums)/2]