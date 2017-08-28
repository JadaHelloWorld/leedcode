# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
#   (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(depth, node):
            if node:
                d[depth].append(node.val)
                helper(depth+1, node.left)
                helper(depth+1, node.right)
        d = collections.defaultdict(list)
        helper(1, root)
        return d.values()[::-1]