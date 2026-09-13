class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0
        for price in prices:
            if(price < lowest):
                lowest = price
            res = max(res, price-lowest)
        return res

        
        