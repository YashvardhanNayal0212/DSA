class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        s=float("inf")
        for i in range(len(tasks)):
            n=sum(tasks[i])
            s=min(s,n)
        return s