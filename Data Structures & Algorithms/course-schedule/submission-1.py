class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def find_incoming(graph: dict[int, List[int]]):
            incoming={node: 0 for node in graph}
            for node in graph:
                neighbors=graph[node]
                for neighbor in neighbors:
                    incoming[neighbor]+=1
            return incoming

        q=deque()
        def topo_sort(graph: dict[int, List[int]]):
            incoming=find_incoming(graph)
            for node in incoming:
                if incoming[node]==0:
                    q.append(node)
            
            while q:
                cur_node=q.popleft()
                for neighbor in graph[cur_node]:
                    incoming[neighbor]-=1
                    if incoming[neighbor]==0:
                        q.append(neighbor)
            print(incoming)
            all_zeros = all(value==0 for value in incoming.values())
            return all_zeros


        graph={i: [] for i in range(numCourses)}
        for preq in prerequisites:
            preq[0],preq[1]
            graph[preq[1]].append(preq[0])
        # print(graph)
        return topo_sort(graph)