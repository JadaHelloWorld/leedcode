# A linked list is given such that each node contains an additional random pointer
#   which could point to any node in the list or null.
#
# Return a deep copy of the list.


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        point = head
        while point:
            node = RandomListNode(point.label)
            point.next, node.next, point = node, point.next, point.next

        point = head
        while point:
            if point.random:
                point.next.random = point.random.next
            point = point.next.next

        root = head.next
        pold = head
        pnew = root
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return root