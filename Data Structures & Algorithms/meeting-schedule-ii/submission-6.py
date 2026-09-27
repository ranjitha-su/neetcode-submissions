"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop
from math import inf
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if meetings overal - different rooms.
        # How do I figure, they overlap
        # start1<=start2<end1
        count=0
        # stores all the meeting intervals as they 
        q=[]
        intervals.sort(key=lambda interval:interval.start)
        for i in range(len(intervals)):
            cur_interval=intervals[i]
            if i == 0:
                heappush(q,(cur_interval.end,cur_interval.start))
                count+=1
            else:
                q_end, q_start=q[0]
                if cur_interval.start>=q_end:
                    # print(f"Reuse meeting room for {cur_interval.start}>={q_end}, pop({q_start,q_end})")
                    heappop(q)
                    heappush(q,(cur_interval.end,cur_interval.start))
                else:
                    # print(f"New meeting room {cur_interval.start}<{q_end}")
                    heappush(q,(cur_interval.end,cur_interval.start))
                    count+=1
        return count

# q=[(60,110),(70,120)], count=1
# [(0,40),(5,10),(15,20)]
[(0,50),(10,60),(60,110),(70,120),(20,70),(30,80),(40,90),(50,100),(80,130),(90,140),(100,150)]
