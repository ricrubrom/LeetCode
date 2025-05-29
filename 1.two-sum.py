#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            another_num = target-num
            if another_num in nums_dict:
                return (nums_dict[another_num], i)
            nums_dict[num] = i
# @lc code=end
