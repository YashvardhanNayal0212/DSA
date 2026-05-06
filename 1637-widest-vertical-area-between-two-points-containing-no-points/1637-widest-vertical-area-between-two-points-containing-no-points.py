class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        m=0
        points.sort()
        for i in range (1,len(points)):
            n=points[i][0]-points[i-1][0]
            m=max(m,n)
        return m
            