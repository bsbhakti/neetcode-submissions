class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        first = cost[-1]
        second = 0

        i = len(cost)-2
        res=[0]* len(cost) 
        res[-1] = cost[-1]
        while i >=0:
            res[i] = cost[i] + min(first,second)
            second = first
            first = res[i]
            i -=1

        return min(res[0], res[1])
                