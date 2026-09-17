class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_rows,num_cols=len(board), len(board[0])
        def is_box_valid(row_start, row_end, col_start, col_end):
            print(f"board({row_start}, {row_end}, {col_start}, {col_end})")
            hashset=set()
            for i in range(row_start, row_end):
                for j in range(col_start, col_end):
                    # print(f"board[{i}][{j}]")
                    if board[i][j] !='.' and board[i][j] in hashset:
                        # print(f"board[{i}][{j}]")
                        # print(start,end,row_boundary, end_boundary)
                        print(f"returning from here1:board[{i}][{j}]: {board[i][j]}")
                        # print(hashset)
                        return False
                    hashset.add(board[i][j])
                    # print(hashset)
            return True

        hashmap={}
        for i in range(num_rows):
            hashmap.clear()
            for j in range(num_cols):
                if board[i][j] != '.':
                    if board[i][j] in hashmap:
                        print(f"board[{i}][{j}]")
                        print("returning from here2")
                        return False
                    hashmap[board[i][j]]=True
        hashmap.clear()
        for j in range(num_cols):
            hashmap.clear()
            for i in range(num_rows):
                if board[i][j] != '.':
                    if board[i][j] in hashmap:
                        print(f"board[{i}][{j}]")
                        print("returning from here3")
                        return False
                    hashmap[board[i][j]]=True
        
        boundaries=[
            (0,3,0,3), (0,3,3,6), (0,3,6,9),
            (3,6,0,3), (3,6,3,6), (3,6,6,9),
            (6,9,0,3), (6,9,3,6), (6,9,6,9)
        ]
        start,end=0,0
        for boundary in boundaries:
            row_start,row_end,col_start,col_end=boundary
            result = True and is_box_valid(row_start, row_end, col_start, col_end)
            if not result:
                return result
        return result
# 0-3, 0-3
# 3-6, 3-6
# 6-9, 6-9