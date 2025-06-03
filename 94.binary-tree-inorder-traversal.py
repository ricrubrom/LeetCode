#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def travel(self, act,solutions):
        if(act!=None):
            if(act.left!=None):
                self.travel(act.left,solutions)
            solutions.append(act.val)
            if(act.right!=None):
                self.travel(act.right,solutions)
        
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        solutions=[]
        self.travel(root,solutions)
        return solutions
# @lc code=end

