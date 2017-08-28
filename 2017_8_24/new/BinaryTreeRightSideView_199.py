# Given a binary tree, imagine yourself standing on the right side of it,
#   return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(node, depth):
            if node:
                d[depth].append(node.val)
                helper(node.left, depth+1)
                helper(node.right, depth+1)
        d = collections.defaultdict(list)
        helper(root, 0)
        return [x[-1] for x in d.values()]