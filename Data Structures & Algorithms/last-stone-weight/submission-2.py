class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            big = heapq.heappop(stones)
            small = heapq.heappop(stones)
            diff = big - small
    
            if(diff != 0):
                heapq.heappush(stones, diff)
        if(len(stones) == 0):
            return 0
        return abs(stones[0])

        