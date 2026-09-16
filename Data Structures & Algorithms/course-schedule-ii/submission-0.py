from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def find_incoming(graph):
            incoming = {node:0 for node in graph}
            for node in graph:
                for neighbor in graph[node]:
                    incoming[neighbor]+=1
            return incoming

        def topo_sort(graph):
            incoming_edges=find_incoming(graph)
            q = deque()
            level=0
            result=[]
            for node_from_incoming in incoming_edges:
                if incoming_edges[node_from_incoming]==0:
                    q.append(node_from_incoming)
            
            while q:
                level_size=len(q)
                # if level is > 1-> then multiple paths are possible
                for _ in range(level_size):
                    cur_node=q.popleft()
                    result.append(cur_node)
                    for neighbor in graph[cur_node]:
                        incoming_edges[neighbor]-=1
                        if incoming_edges[neighbor]==0:
                            q.append(neighbor)
            if max(incoming_edges.values())>0:
                # cycle exists
                return []
            return result

        graph = {node:[] for node in range(numCourses)}
        for preq in prerequisites:
            # preq[0]:neighbor, preq[1]:node
            graph[preq[1]].append(preq[0])
        return topo_sort(graph)

'''
---------------------
0(popped) 2
---------------------
0->1
2

incoming edges represention:
0:0
1:0
2:0
graph representation
0:[1]
1:[]
2:[]
many valid answers-> multiple topo orderings
not possible -> cycle in a graph -> incoming edges of all nodes won't be zero. some incoming edges will be left
'''