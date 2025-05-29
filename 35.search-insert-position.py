#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while (left <= right):
            mid = (left+right)//2
            if (nums[mid] < target):
                left = mid+1
            elif (nums[mid] > target):
                right = mid-1
            else:
                return mid

        return left
# @lc code=end
