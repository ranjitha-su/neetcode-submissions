class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    


        num_rows,num_cols=len(heights),len(heights[0])
        def get_neighbors(coordinates: tuple[int,int]):
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

        pacific_q=deque()
        atlantic_q=deque()
        pacific_visited=set()
        atlantic_visited=set()
        pacific_result = []
        atlantic_result = []
        result=[]
        for i in range(num_rows):
            for j in range(num_cols):
                if i==0 or j==0:
                    pacific_q.append((i,j))
                    pacific_visited.add((i,j))
                if i==num_rows-1 or j==num_cols-1:
                    atlantic_q.append((i,j))
                    atlantic_visited.add((i,j))
        while pacific_q:
            cur_node=pacific_q.popleft()
            pacific_result.append(cur_node)
            cur_r,cur_c=cur_node
            for neighbor in get_neighbors(cur_node):
                nr,nc=neighbor
                if heights[nr][nc]<heights[cur_r][cur_c] or neighbor in pacific_visited:
                    continue
                pacific_q.append(neighbor)
                pacific_visited.add(neighbor)
        while atlantic_q:
            cur_node=atlantic_q.popleft()
            atlantic_result.append(cur_node)
            cur_r,cur_c=cur_node
            for neighbor in get_neighbors(cur_node):
                nr,nc=neighbor
                if heights[nr][nc]<heights[cur_r][cur_c] or neighbor in atlantic_visited:
                    continue
                atlantic_q.append(neighbor)
                atlantic_visited.add(neighbor)
        
        for cell in pacific_result:
            if cell in atlantic_result:
                result.append(cell)
        print(result)
        return result


