from heapq import heappush, heappop
from math import inf
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        def get_neighbors(adjacency_list: dict[int, list[int]], node: int):
            return adjacency_list[node]

        def minimum_time(adjacency_list: dict[int, list[int]], src:int)->int:
            distances=[inf]*n
            print(distances)
            q=[(0, src)]
            distances[src-1]=0
            while q:
                distance_from_src, cur_node=heappop(q)
                if distance_from_src>distances[cur_node-1]:
                    continue
                for neighbor, weight in get_neighbors(adjacency_list, cur_node):
                    neighbor_weight = distances[cur_node-1]+weight
                    if distances[neighbor-1]<=neighbor_weight:
                        continue
                    distances[neighbor-1]=neighbor_weight
                    heappush(q,(distances[neighbor-1],neighbor))
            if inf in distances:
                return -1
            return max(distances)
        adjacency_list={i: [] for i in range(1,n+1)}
        for time in times:
            adjacency_list[time[0]].append((time[1], time[2]))
        return minimum_time(adjacency_list, k)

