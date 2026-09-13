class Solution:
    def rob(self, nums: List[int]) -> int:
        def sub(i,j):
            rob1 = 0
            rob2 = 0
          
            for n in range(i,j):
                print(n)
                print("h")
                temp = max(rob1 + nums[n], rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        if (len(nums) ==1):
                return nums[0]
        return max(sub(0,len(nums)-1), sub(1,len(nums)))
        