class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        s=arrivalTime+delayedTime
        if s>24:
            return s%24
        elif s==24 or s%24==0:
            return 0
        else:
            return s