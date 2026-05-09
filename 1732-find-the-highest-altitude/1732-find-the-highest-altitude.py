class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        r=[0]
        for i in range(len(gain)):
            r.append(r[i]+gain[i])
        return max(r)