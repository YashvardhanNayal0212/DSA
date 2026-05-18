class Solution:
    def minElement(self, nums: List[int]) -> int:
        m = float("inf")

        for num in nums:
            s = 0

            while num > 0:
                s += num % 10
                num //= 10

            m = min(m, s)

        return m