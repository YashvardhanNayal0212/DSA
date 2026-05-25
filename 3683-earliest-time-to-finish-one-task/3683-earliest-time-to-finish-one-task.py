class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        s=sum(tasks[0])
        for i in range(1, len(tasks)):
            n=sum(tasks[i])
            s=min(s,n)
        return s