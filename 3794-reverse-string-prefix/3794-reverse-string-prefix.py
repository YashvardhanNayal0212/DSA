class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        a=s[:k][::-1]
        b=s[k:len(s)]
        return a+b