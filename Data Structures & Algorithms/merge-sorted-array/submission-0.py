class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        zeroPos = len(nums1) - 1
        nums1R = m - 1
        nums2R = n - 1

        while nums1R >= 0 and nums2R >= 0:
            if nums1[nums1R] >= nums2[nums2R]:
                nums1[zeroPos] = nums1[nums1R]
                nums1[nums1R] = 0
                nums1R -= 1
            else:
                nums1[zeroPos] = nums2[nums2R]
                nums2R -= 1
            zeroPos -= 1
        
        while nums2R >= 0:
            nums1[zeroPos] = nums2[nums2R]
            nums2R -= 1
            zeroPos -= 1