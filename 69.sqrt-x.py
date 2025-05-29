#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 1
        right = x
        while left <= right:
            mid = (right+left)//2
            p = mid*mid
            if p < x:
                left = mid+1
            elif p > x:
                right = mid-1
            else:
                return mid
        return right
# @lc code=end
