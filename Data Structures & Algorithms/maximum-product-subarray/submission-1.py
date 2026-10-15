class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minPro, maxPro = 1,1
        for i in nums:
            # if i == 0:
            #     minPro,maxPro =1,1
            #     # continue
            # else:
                t =minPro *i 
                minPro = min(minPro *i, i, maxPro*i)
                maxPro = max(maxPro*i, i, t)
                res = max(res,maxPro)
                # print(i, minPro,maxPro)
        return res

        