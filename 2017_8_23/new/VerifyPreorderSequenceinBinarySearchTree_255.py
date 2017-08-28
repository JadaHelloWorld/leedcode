# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
#
# You may assume each number in the sequence is unique.
#
# Follow up:
# Could you do it using only constant space complexity?
import sys


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        min = -sys.maxint-1
        for x in preorder:
            if x < min: return False
            while stack and stack[-1]<x:
                min = stack.pop()

            stack.append(x)
        return True