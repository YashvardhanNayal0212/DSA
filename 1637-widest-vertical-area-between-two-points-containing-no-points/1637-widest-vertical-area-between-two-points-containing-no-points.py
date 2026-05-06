class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr=[]
        for i in range (len(points)):
            arr.append(points[i][0])
        arr.sort()
        diff=0
        for i in range (1,len(arr)):
            d=arr[i]-arr[i-1]
            diff=max(diff,d)
        return diff