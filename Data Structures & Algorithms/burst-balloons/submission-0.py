class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        # print(nums)
        def recur(l,r):
            if l >r :
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += recur(i+1,r) + recur(l,i-1)
                if (l,r) in dp:
                    dp[(l,r)] = max(dp[(l,r)],coins)
                else:
                    dp[(l,r)] = coins
            return dp[(l,r)]
        return recur(1,len(nums)-2)
            