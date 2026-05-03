class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        org=num
        while num!=0:
            a=num%10
            if org%a==0:
                count+=1
            num=num//10
        return count