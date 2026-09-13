class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while (len(self.nums) > self.k):
            heapq.heappop(self.nums)
        
        

    def add(self, val: int) -> int:
        # self.nums.heappush(val)
        heapq.heappush(self.nums, val)
        if(len(self.nums) > self.k):
            heapq.heappop(self.nums)
        return self.nums[0]
        # self.nums.append(val)
        # print(self.nums)
        # self.nums = self.nums.sort()
        # print(self.nums)
        # print(self.nums)
        # return (self.nums[self.k -1])
        
kthLargest =  KthLargest(3, [1, 2, 3, 3]);
print(kthLargest.nums)

# # kthLargest.add(3);   // return 3
# kthLargest.add(5);   // return 3
# kthLargest.add(6);   // return 3
# kthLargest.add(7);   // return 5
# kthLargest.add(8);   // return 6
