#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def travel(self, act, max, depth):
        if(act==None):
            return depth
        aux=self.travel(act.left, max, depth+1)
        if(aux>max):
            max=aux
        aux=self.travel(act.right, max, depth+1)
        if(aux>max):
            max=aux
        return max

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max=0
        max=self.travel(root, max, 0)
        return max
# @lc code=end

