#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        for i, c in enumerate(s):
            act = roman_dict[c]
            if i + 1 < len(s) and roman_dict[s[i + 1]] > act:
                num = num-act
            else:
                num = num+act
        return num

# @lc code=end
