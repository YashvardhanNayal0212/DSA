class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        a=[]
        m=float("inf")
        for i in range(1,int(area**0.5 )+1):
            if area%i==0:
                diff=abs(i-area//i)
                m=min(diff,m)
                a=[area//i,i]
        return a
