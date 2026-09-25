from math import inf
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        smallest_start,largest_end=0,inf
        intervals.sort()
        output=[]
        for i in range(len(intervals)):
            cur_interval=intervals[i]
            if i==0:
                smallest_start=cur_interval[0]
                largest_end=cur_interval[1] 
            else:
                if smallest_start<=cur_interval[0]<=largest_end:
                    print("yes overlap")
                    # yes overlap
                    smallest_start=min(smallest_start,cur_interval[0])
                    largest_end=max(largest_end, cur_interval[1])
                else:
                    # no overlap
                    output.append([smallest_start,largest_end])
                    smallest_start=cur_interval[0]
                    largest_end=cur_interval[1]
        output.append([smallest_start, largest_end])
        return output
    
    #   [1,3][1,5][6,7] -> [1,5][6,7]
#     [1,2][3,5][4,8][7,9][11,12]
#     [1,3][2,5][4,6][7,8] -> [1,6],[7,8]
#     [1,3][2,5][6,7] -> [1,5],[6,7]
#     [1,3][4,6] -> [1,3],[4,6]
#     [1,3][4,6][5,7] -> [1,3][4,7]
#     [1,3][2,4][3,5] -> [1,5]
    # > [1,4][0,5]
#     smallest_start=1
#     largest_end=4
            
