class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = []

        for i in nums:
            if nums.count(i) == 1:
                s.append(i)

        return sum(s)