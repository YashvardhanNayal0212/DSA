class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        a=[]
        for i in range (len(order)):
            if order[i] in friends:
                a.append(order[i])
        return a