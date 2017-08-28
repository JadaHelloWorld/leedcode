# Given n non-negative integers representing an elevation map where the width of each bar is 1,
#   compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
#   In this case, 6 units of rain water (blue section) are being trapped.


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3: return 0
        left = 0
        right = len(height) - 1
        l_m = 0
        r_m = 0

        res = 0
        while right > left:

            if height[left] <= height[right]:
                l_m = max(height[left], l_m)
                res += l_m - height[left]
                left += 1

            else:
                r_m = max(height[right], r_m)
                res += r_m - height[right]
                right -= 1

        return res