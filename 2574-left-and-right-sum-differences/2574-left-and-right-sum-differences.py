class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=[0]
        r=[0]
        sum=num=0
        for i in range (1,len(nums)):
            sum+=nums[i-1]
            l.append(sum)
        for j in range(len(nums)-2,-1,-1):
            num+=nums[j+1]
            r.append(num)
        r=r[::-1]
        for i in range (len(nums)):
            l[i]=abs(l[i]-r[i])
        return l