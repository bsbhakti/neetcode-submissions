class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = sum(nums)
        actual = (len(nums) * (len(nums)+1))//2
        # print(actual-curr)
        return actual - curr
        