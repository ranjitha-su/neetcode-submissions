"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from math import inf
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # intervals.sort()
        intervals.sort(key=lambda interval: interval.start)
        print([[x.start,x.end] for x in intervals])
        smallest_start,largest_end=0,inf
        for i in range(len(intervals)):
            cur_interval=intervals[i]
            if i==0:
                smallest_start=cur_interval.start
                largest_end=cur_interval.end
            else:
                if smallest_start<=cur_interval.start<largest_end:
                    return False
            smallest_start=cur_interval.start
            largest_end=cur_interval.end
        return True