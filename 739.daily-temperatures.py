#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures):
        stack = deque()
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            if not stack:
                stack.appendleft(i)
                res[i] = 0
            else:
                while stack and temperatures[i] >= temperatures[stack[0]]:
                    stack.popleft()

                if not stack:
                    res[i] = 0
                else:
                    res[i] = stack[0] - i

                stack.appendleft(i)

        return res


# @lc code=end
