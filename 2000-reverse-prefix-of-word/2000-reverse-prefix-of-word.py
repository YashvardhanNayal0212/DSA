class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s=0
        for i in range(len(word)):
            if word[i]==ch:
                s=i
                break
        if s==0:
            return word
        a=word[:s+1][::-1]
        b=word[s+1:]
        return a+b