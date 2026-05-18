class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        n=purchaseAmount%10
        if n==0:
            return 100-purchaseAmount
        elif n<5 and n>0:
            purchaseAmount-=n
        else:
            purchaseAmount+=10-n
        return 100-purchaseAmount