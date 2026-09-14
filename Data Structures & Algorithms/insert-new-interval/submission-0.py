class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals.append(newInterval)
        intervals = sorted(intervals)
        if len(intervals) == 1:
            return intervals
        # (1,3)
        # (2,5)

        prev = intervals[0]
        for i in range(1,len(intervals)):
            prev_a = prev[0]
            prev_b = prev[1]
            a = intervals[i][0]
            b = intervals[i][1]
            # print("prev", prev_a, prev_b)
            # print("curr", a,b)
            if a <= prev_b:
                prev = [min(prev_a,a), max(prev_b,b)]
            else:
                res.append(prev)
                prev = [a,b]
        res.append(prev)
        return res