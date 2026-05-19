class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n=m=0
        while n<len(nums1) and m<len(nums2):
            if nums1[n]==nums2[m]:
                return nums1[n]
            elif nums1[n]>nums2[m]:
                m+=1
            else:
                n+=1
        return -1