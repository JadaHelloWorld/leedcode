# You are given two non-empty linked lists representing two non-negative integers.
#   The digits are stored in reverse order and each of their nodes contain a single digit.
#   Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        point = root
        last_pre = 0
        while l1 and l2:
            cur_num = l1.val + l2.val + last_pre
            if cur_num >= 10:
                last_pre = 1
                cur_num -= 10
            else:
                last_pre = 0
            l1 = l1.next
            l2 = l2.next
            point.next = ListNode(cur_num)
            point = point.next

        sub_last = l1 or l2
        while sub_last:
            cur_num = sub_last.val + last_pre
            if cur_num >= 10:
                last_pre = 1
                cur_num -= 10
            else:
                last_pre = 0

            sub_last = sub_last.next
            point.next = ListNode(cur_num)
            point = point.next

        if last_pre:
            point.next = ListNode(last_pre)
        return root.next
        # p = l1
        # q = l2
        # dummy_head = ListNode(0)
        # node = dummy_head
        # carry = 0
        # while p or q:
        #     pval = p.val if p else 0
        #     qval = q.val if q else 0
        #     num = pval + qval + carry
        #     carry = 1 if num >= 10 else 0
        #     digit = num % 10
        #     node.next = ListNode(digit)
        #     # Move all pointers
        #     node = node.next
        #     p = p.next if p else None
        #     q = q.next if q else None
        # if carry == 1:
        #     node.next = ListNode(1)
        # return dummy_head.next



