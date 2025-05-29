#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s=s.strip()
        if len(s) == 0:
            return 0
        i = len(s)-1
        length = 0
        while i > 0 and s[i] == ' ':
            i -= 1
        while i > 0 and s[i] != ' ':
            length += 1
            i -= 1
        if i == 0 and s[i] != ' ':
            length += 1
        return length
# @lc code=end
