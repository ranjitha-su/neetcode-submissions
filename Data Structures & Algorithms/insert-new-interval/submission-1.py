class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output=[]
        # if newInterval[start]>cur_interval[end]- no overlap cur interval is before new interval. 
        # if newInterval[end]<curInterval[start] - no overal cur interval is after new interval.
        # if curInterval[start]<newInterval[start]<curInterval[end] - overlap
         
        for i in range(len(intervals)):
            curInterval=intervals[i]
            if newInterval[0]>curInterval[1]:
                output.append(curInterval)
            elif newInterval[1]<curInterval[0]:
                output.append(newInterval)
                output.extend(intervals[i:])
                return output
            elif curInterval[0]<=newInterval[0]<=curInterval[1] or curInterval[0]<=newInterval[1]<=curInterval[1]:
                newInterval[0]=min(curInterval[0], newInterval[0])
                newInterval[1]=max(curInterval[1], newInterval[1])
        
        output.append(newInterval)
        return output

#  cur=[1,3], new=[2,5]  
#  cur=[4,6], new=[1,5]        
    