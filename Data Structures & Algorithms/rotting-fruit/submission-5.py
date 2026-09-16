from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows,num_cols=len(grid), len(grid[0])
        def get_neighbors(coordinates: tuple[int,int]):
            row,col=coordinates
            delta_row=[-1, 0, 1, 0]
            delta_col=[0, 1, 0, -1]
            neighbors=[]
            for i in range(len(delta_row)):
                neighbor_row=row+delta_row[i]
                neighbor_col=col+delta_col[i]
                if 0<=neighbor_row<num_rows and 0<=neighbor_col<num_cols:
                    neighbors.append((neighbor_row, neighbor_col))
            return neighbors

        q = deque()
        level=0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j]!=2:
                    continue
                q.append((i,j))
        
        while q:
            level_size=len(q)
            rotted=False
            for _ in range(level_size):
                cur_node=q.popleft()
                for neighbor in get_neighbors(cur_node):
                    
                    r,c=neighbor
                    if grid[r][c]==2 or grid[r][c]==0:
                        continue
                    print(f"Rotting neighbors: {(r,c)}")
                    q.append(neighbor)
                    grid[r][c]=2
                    rotted=True
            if rotted:
                level+=1
            print(f"Incrementing level to {level}")
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j]==1:
                    return -1
        return level
                    


# 0 - empty cell
# 1- fresh fruit
# 2- rotten fruit                                                                                             