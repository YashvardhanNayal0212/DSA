class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        arr=[]
        diff=l=w=0
        for i in range (1,int(area**0.5)+1):
            if area%i==0:
                w=i
                l=area//i
                diff=min(diff,l,w)
        arr.append(l)
        arr.append(w)
        return arr