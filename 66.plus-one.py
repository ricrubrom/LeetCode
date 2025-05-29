
#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
from collections import deque


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = deque(digits)
        i = len(digits)-1
        digits[i] += 1
        while i >= 0 and digits[i] >= 10:
            if digits[i] >= 10:
                digits[i] = digits[i] % 10
                if i == 0:
                    digits.appendleft(1)
                else:
                    digits[i-1] += 1
            i -= 1
        if digits[i] >= 10 and i == 0:
            digits.appendleft(1)
        digits = list(digits)
        return digits
# @lc code=end
