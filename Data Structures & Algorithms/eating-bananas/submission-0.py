class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high
        while low <= high:
            mid = (low+high)//2
            total = 0
            for i in piles:
                total += math.ceil(i/mid)
            if total > h:
                low = mid+1
            else:
                res = mid
                high = mid -1
        return res        