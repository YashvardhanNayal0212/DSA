class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum=1
        n=int(num**0.5)
        for i in range(2,n+1):
            if num%i==0:
                sum+=i
                sum+=num//i
        if num==1:
            return False
        else: 
            return sum==num