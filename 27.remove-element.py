#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while(right>=left):
            if nums[right]==val:
                right-=1
                continue
            if nums[left]==val:
                nums[left]=nums[right]
                right-=1
            left+=1
        return left
# @lc code=end

