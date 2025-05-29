#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if (m > 0):
            nums1_copia = nums1[:m]
        i = 0
        j = 0
        k = 0

        while (i < m) and (j < n):
            if nums1_copia[i] > nums2[j]:
                nums1[k] = nums2[j]
                j += 1
            else:
                nums1[k] = nums1_copia[i]
                i += 1
            k += 1

        while (i < m):
            nums1[k] = nums1_copia[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            k += 1
            j += 1

# @lc code=end
