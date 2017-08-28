# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ? k ? BST's total elements.
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
#   How would you optimize the kthSmallest routine?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def helper(node):
            if not node or len(count) == k: return
            helper(node.left)
            if len(count) == k: return
            count.append(node.val)
            helper(node.right)
            
        count = []
        helper(root)
        return count[-1]