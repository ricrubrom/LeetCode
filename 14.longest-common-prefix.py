#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        first = strs[0]
        last = strs[-1]
        prefix = ""
        for i in range(0, min(len(first), len(last))):
            c = first[i]
            if c != last[i]:
                break
            prefix += c
        return prefix

# @lc code=end
