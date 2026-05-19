class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a=(len(nums1))-m
        for i in range (a):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
        return nums1