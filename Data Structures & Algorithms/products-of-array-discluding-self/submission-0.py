class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre = [1] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        curr = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            pre[i] = pre[i] * curr
            curr *= nums[i]
        # print(pre,su)
        # res = pre *su
        return pre
        