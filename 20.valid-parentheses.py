#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = ['(', '[', '{']
        closed = [')', ']', '}']
        aux = []
        for c in s:
            if c in open:
                aux.append(c)
            elif c in closed:
                if (not aux):
                    return False
                cc = aux.pop()
                if c == ')':
                    if cc != '(':
                        return False
                elif c == ']':
                    if cc != '[':
                        return False
                elif c == '}':
                    if cc != '{':
                        return False
        return not aux

# @lc code=end
