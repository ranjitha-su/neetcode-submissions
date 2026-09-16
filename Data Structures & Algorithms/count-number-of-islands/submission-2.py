from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows,num_cols=len(grid),len(grid[0])
        def get_neighbors(coordinates:int):
            row,col=coordinates
            delta_row=[-1,0,1,0]
            delta_col=[0,1,0,-1]
            neighbors=[]
            for i in range(len(delta_row)):
                neighbor_row=row+delta_row[i]
                neighbor_col=col+delta_col[i]
                if 0<=neighbor_row<num_rows and 0<=neighbor_col<num_cols:
                    neighbors.append((neighbor_row,neighbor_col))
            return neighbors
        
        q=deque()
        # level=0
        visited=set()
        island_count=0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j]!="1" or (i,j) in visited:
                    continue
                q.append((i,j))
                visited.add((i,j))
                while q:
                    # level_size=len(q)
                    cur_node=q.popleft()
                    for neighbor in get_neighbors(cur_node):
                        r,c=neighbor
                        if neighbor in visited or grid[r][c]=="0":
                            continue
                        q.append(neighbor)
                        visited.add(neighbor)
                island_count+=1
        return island_count