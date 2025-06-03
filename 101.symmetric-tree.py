#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def travel(self, p, q):
        symmetric=True
        if (p!=None):
            if (q!=None):
                if(p.val!=q.val):
                    symmetric=False
                if(symmetric):
                    symmetric=self.travel(p.left,q.right)
                if(symmetric):
                    symmetric=self.travel(p.right,q.left)
            else:
                symmetric=False
        elif (q!=None):
            symmetric=False
        return symmetric
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if(root==None):
            return False
        return self.travel(root.left, root.right)
# @lc code=end

