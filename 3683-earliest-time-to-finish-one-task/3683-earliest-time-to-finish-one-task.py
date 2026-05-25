class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        s=float("inf")
        for i in tasks:
           
            s=min(s,sum(i))
        return s