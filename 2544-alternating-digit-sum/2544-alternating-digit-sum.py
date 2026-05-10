class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=[]
        sum=0
        while n!=0:
            num=n%10
            s.append(num)
            n//=10
        s[:]=s[::-1]
        for i in range (len(s)):
            if i==0 or i%2==0:
                sum+=s[i]
            elif i==1 or i%2==1:
                sum-=s[i]
        return sum