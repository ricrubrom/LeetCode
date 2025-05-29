#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if (head == None):
            return None
        last = head
        act = last.next
        while (act != None):
            if act.val == last.val:
                while (act != None and act.val == last.val):
                    act = act.next
                last.next = act
                continue
            else:
                last = act
                act = act.next
        return head

# @lc code=end
