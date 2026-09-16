"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def s(n):
            return n.start
        intervals = sorted(intervals,key=s)
        if len(intervals) <= 1:
            return True
        prev = intervals[0]
        for i in range(1, len(intervals)):
            prev_start = prev.start
            prev_end = prev.end
            curr_start = intervals[i].start
            curr_end = intervals[i].end

            if curr_start < prev_end:
                return False
            prev = intervals[i]
        return True



