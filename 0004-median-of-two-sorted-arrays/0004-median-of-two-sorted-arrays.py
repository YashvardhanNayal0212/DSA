class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L=R=0
        arr=[]
        while L<len(nums1) and R<len(nums2):
            if nums1[L]>nums2[R]:
                arr.append(nums2[R])
                R+=1
            elif nums1[L]<nums2[R]:
                arr.append(nums1[L])
                L+=1
            else:
                arr.append(nums1[L])
                arr.append(nums2[R])
                R+=1
                L+=1
        while L<len(nums1):
            arr.append(nums1[L])
            L+=1
        while R<len(nums2):
            arr.append(nums2[R])
            R+=1
        
        n=len(arr)
        if n%2==1:
            return (arr[n//2])
        return ((arr[n//2]+arr[n//2-1])/2)
        