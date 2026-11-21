class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for i in points:
            d = -math.sqrt( (0-i[0])**2 + (0-i[1])**2 )
            # print(d, i)

            if len(heap) < k:
                heapq.heappush(heap,(d,i))
            else:
                top = heap[0][0]
                # print("top", top)
                if top < d:
                    # print("popped and pushed")
                    heapq.heappop(heap)
                    heapq.heappush(heap,(d,i))
        res = []
        while heap:
            pop = heapq.heappop(heap)
            # print(pop)
            res.append(pop[1])
        return res

        