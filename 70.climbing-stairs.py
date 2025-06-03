#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        num1=1
        num2=2
        for i in range(3,n+1):
            aux=num1
            num1=num2
            num2=aux+num2
        return num2    
# @lc code=end

