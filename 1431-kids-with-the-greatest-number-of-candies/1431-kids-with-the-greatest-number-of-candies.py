class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr=[0]*len(candies)
        m=max(candies)
        for i in range (len(candies)):
            n=candies[i]+extraCandies
            if n>=m:
                arr[i]=True
            else:
                arr[i]=False
        return arr