class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        total = 0
        ret = None
        if sum(cost) > sum(gas):
            return -1
        for i in range(len(cost)):
            diff = total + gas[i] - cost[i]
            # print("diff", diff)
            if diff <0 :
                total  = 0
                ret = None
            else:
                total = diff
                if ret is None:
                    ret = i
                # print(total,ret,i)
        return ret