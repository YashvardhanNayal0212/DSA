class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c=[0,0]
        org=c[:]
        for i in moves:
            if i=="U":
                c[0]+=1
            elif i=="D":
                c[0]-=1
            elif i=="R":
                c[1]+=1
            elif i=="L":
                c[1]-=1
        return org==c