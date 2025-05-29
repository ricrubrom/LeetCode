#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def recursion(self, ans, strs,  n, open, closed):
        if (open == closed and closed == n):
            return ans.append(strs)
        if (open < n):
            self.recursion(ans, strs+'(', n, open+1, closed)
        if (closed < n and open > closed):
            self.recursion(ans, strs+')', n, open, closed+1)
        return

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self.recursion(ans, '(', n, 1, 0)
        return ans


# @lc code=end
