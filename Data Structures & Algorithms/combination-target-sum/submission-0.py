class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def search(i,total,curr):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total >= target:
                return
            curr.append(nums[i])
            # print("added ", nums[i])
            search(i,total+nums[i],curr)
            curr.pop()
            # print("right ")
            
            search(i+1, total, curr)
        
        search(0,0,[])
        return res
