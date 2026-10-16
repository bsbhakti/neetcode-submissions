class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for i in range(k):
            heapq.heappush(heap,nums[i])
        for i in range(k, len(nums)):
            sm = heap[0]
            # print("current", sm)
            if sm < nums[i]:
                # print("pooping", nums[i])
                heapq.heappop(heap)
                heapq.heappush(heap,nums[i])

      
        ret = heapq.heappop(heap)
        return ret
        