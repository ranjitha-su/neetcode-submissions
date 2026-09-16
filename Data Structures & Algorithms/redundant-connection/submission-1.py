class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find_root(x: int):
            if parent[x]==x:
                return x
            parent[x]= find_root(parent[x])
            return parent[x]
        
        def union(x:int, y:int):
            output=[]
            rx=find_root(x)
            ry=find_root(y)
            if rx==ry:
                output=[x,y]
                print(output)
                return output
            parent[rx]=ry
            return output

        

        parent={}
        for edge in edges:
            if edge[0] not in parent:
                parent[edge[0]]=edge[0]
            if edge[1] not in parent:
                parent[edge[1]]=edge[1]

        for edge in edges:
            output= union(edge[0],edge[1])
            if output:
                return output
       

# union(1,2)
#     find_root(1)-> 1
#     find_root(2)-> 2
# union(1,3)
#     find_root(1)-> 2
#     find_root(3)-> 3
# union(3,4)
#     find_root(3)->3
#     find_root(4)->4
# union(2,4)
#     find_root(2)->4
#     find_root(4)->4
# parent={
#     1:2,
#     2:3,
#     3:4,
#     4:4
# }
            