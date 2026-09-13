class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cache = {}
        def recur(i, buy):
            nonlocal profit
            if i >= len(prices):
                return 0
            
            elif (i,buy) in cache:
                return cache[(i,buy)]
            elif buy: #true
                #sell
                a = prices[i] + recur(i+2, False)
                #nothing
                b = recur(i+1, buy)
                # print("found",a,b)
                # profit = max(profit, max(a,b))
                cache[(i,buy)] = max(a,b)
                # print("cache", cache) 
                return max(a,b)
                
            else: #False
                #buy
                a = recur(i+1, True) - prices[i]
                #no
                b = recur(i+1, buy)
                # print("found",a,b)
                cache[(i,buy)] = max(a,b)
                # profit = max(profit, max(a,b))


                return max(a,b)
        print(cache)
        recur(0,False)
        return cache[(0,False)] 

        