class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        cur = nums[0]

        for n in nums[1:]:
            if (cur < 0):
                cur = 0
            cur += n
            m = max(cur,m)
        return m

        