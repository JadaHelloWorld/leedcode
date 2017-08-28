# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None): return 0
        result = 1
        q = collections.deque([root])
        while q:
            next_q = collections.deque([])
            while q:
                n = q.popleft()
                if n.left:
                    next_q.append(n.left)
                if n.right:
                    next_q.append(n.right)

            if (next_q):
                result += 1
            q = next_q
            next_q = q

        return result