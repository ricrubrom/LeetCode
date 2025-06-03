#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1=int(a,2)
        num2=int(b,2)
        res=num1+num2
        return bin(res)[2:] #Saca el 0b
# @lc code=end

