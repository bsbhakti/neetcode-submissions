class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        query_map = {}
        for i, q in enumerate(queries):
            if q not in query_map:
                query_map[q] = []
            query_map[q].append(i)
        print(query_map)

        intervals.sort()
        queries.sort()

        q = 0
        my_heap = []
        res = [-1] * len(queries)
        ind = 0

        print(query_map)


        for i in range(len(queries)):
            print(queries[i],"k")
            while ind < len(intervals) and intervals[ind][0] <= queries[i]:
                heapq.heappush(my_heap,(intervals[ind][1]-intervals[ind][0]+1, intervals[ind][0], intervals[ind][1]))
                ind +=1
            popped = None
            if len(my_heap):
                popped = heapq.heappop(my_heap)
                while len(my_heap) and popped and popped[2] < queries[i]:
                    popped = heapq.heappop(my_heap)
                if popped[1] <= queries[i] and popped[2] >= queries[i]:
                    for idx in query_map[queries[i]]:
                        # res[idx] = answer
                        res[idx] = popped[0]
                    heapq.heappush(my_heap,(popped[0], popped[1], popped[2]))



        return res