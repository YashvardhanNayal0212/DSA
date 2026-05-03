class Solution:
    def isThree(self, n: int) -> bool:
        count=2
        num=int(n//2)
        for i in range (2,num+1):
            if n%i==0:
                count+=1
        return count==3