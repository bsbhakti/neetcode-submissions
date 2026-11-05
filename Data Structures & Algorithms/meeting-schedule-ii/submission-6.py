"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals = sorted(intervals,key=lambda interval: interval.start)
        prev_start = intervals[0].start
        prev_end = intervals[0].end
        # for i in intervals:
            ##print(i.start)
        # ##print(interval)
        res = 1
        heap = []
        heapq.heappush(heap,prev_end)
        for i in range(1,len(intervals)):
            new_start = intervals[i].start
            new_end = intervals[i].end
            top = heap[0]

            if new_start < top:
                res +=1
                heapq.heappush(heap, new_end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, new_end)
            #print("top",top, "curr start", new_start, "roo", res)
            
        # if not res:
        #     res +=1
        return res



        