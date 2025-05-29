#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if (list1 == None):
            if (list2 == None):
                return None
            else:
                return list2
        elif (list2 == None):
            return list1

        aux1 = list1
        aux2 = list2
        if (aux1.val < aux2.val):
            ans = ListNode(aux1.val)
            aux1 = aux1.next
        else:
            ans = ListNode(aux2.val)
            aux2 = aux2.next
        last = ans
        while (aux1 != None and aux2 != None):
            if (aux1.val < aux2.val):
                last.next = ListNode(aux1.val)
                last = last.next
                aux1 = aux1.next
            else:
                last.next = ListNode(aux2.val)
                last = last.next
                aux2 = aux2.next
        while aux1 != None:
            last.next = ListNode(aux1.val)
            last = last.next
            aux1 = aux1.next
        while aux2 != None:
            last.next = ListNode(aux2.val)
            last = last.next
            aux2 = aux2.next
        return ans


# @lc code=end
