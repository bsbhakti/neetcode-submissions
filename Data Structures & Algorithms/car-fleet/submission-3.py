class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [None] * len(position)
        for ind,i in enumerate(position):
            arr[ind] = [position[ind], speed[ind]]
        arr = sorted(arr)
        # print(arr)
        res = len(position)
        prev = None
        for i in range(len(arr)-1,-1,-1):
            curr = (target-arr[i][0])/ arr[i][1]
            if prev != None and curr <= prev:
                res -=1
            else:
                prev = curr
        return res