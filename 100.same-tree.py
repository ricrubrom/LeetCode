#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def travel(self, p_act, q_act):
        equals=True
        if(p_act!=None):
            if(q_act!=None):
                if p_act.val!=q_act.val:
                    equals= False
                if(equals):
                    equals=self.travel(p_act.left, q_act.left)
                if(equals):
                    equals=self.travel(p_act.right, q_act.right)
            else:
                equals=False
        else:
            if(q_act!=None):
                return False
        return equals
    
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        equals=self.travel(p,q)
        return equals


# @lc code=end

