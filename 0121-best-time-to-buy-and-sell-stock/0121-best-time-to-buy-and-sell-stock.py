class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MinPrice=float('inf')
        MaxPrice=0
        for i in range(len(prices)):
            if prices[i]<MinPrice:
                MinPrice=prices[i]
            p=prices[i]-MinPrice
            if MaxPrice<p:
                MaxPrice=p
        return MaxPrice
        