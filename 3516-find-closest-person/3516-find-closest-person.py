class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        num1=abs(y-z)
        num2=abs(x-z)
        if num1<num2:
            return 2
        elif num1==num2: return 0
        else: 
            return 1