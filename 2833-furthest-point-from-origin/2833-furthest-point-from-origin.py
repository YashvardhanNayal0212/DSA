class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=r=blank=0
        for char in moves:
            if char=="L":
                l+=1
            elif char=="R":
                r+=1 
            else:
                blank+=1
        return abs(l-r)+blank