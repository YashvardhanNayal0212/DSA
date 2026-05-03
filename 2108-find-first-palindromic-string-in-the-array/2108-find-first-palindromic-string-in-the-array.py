class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for char in words:
            if char==char[::-1]:
                return char
        return ""