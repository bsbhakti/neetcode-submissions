class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            mid = (l+r)//2
            print(nums[l], nums[mid], nums[r])
            if nums[mid] <= nums[r]:
            
                r = mid
            else:
                l = mid+1
        return nums[r]
        
        