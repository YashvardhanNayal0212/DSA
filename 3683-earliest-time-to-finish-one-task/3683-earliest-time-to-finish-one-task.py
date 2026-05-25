class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        s=float("inf")
        for i in tasks:
            n=sum(i)
            s=min(s,n)
        return s