class Solution:
    def minimumSum(self, num: int) -> int:
        arr=[]
        while num>0:
            n=num%10
            arr.append(n)
            num//=10
        arr.sort()
        a=arr[0]*10+arr[2]
        b=arr[1]*10+arr[3]
        return a+b