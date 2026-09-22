class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search(row:int):
            print(f"Search in row {row}")
            left,right=0,n-1
            while left<=right:
                mid=(left+right)//2
                if target==matrix[row][mid]:
                    return True
                elif target<matrix[row][mid]:
                    right=mid-1
                else:
                    left=mid+1
            return False

        m,n=len(matrix),len(matrix[0])
        start_row,end_row=0,m-1
        while start_row<=end_row:
            mid_row=(start_row+end_row)//2
            if target==matrix[mid_row][0] or target==matrix[mid_row][n-1]:
                return True
            elif target>matrix[mid_row][0] and target<matrix[mid_row][n-1]:
                # binary search on mid_row
                return bin_search(mid_row)
            elif target<matrix[mid_row][0]:
                print("decrement end row")
                end_row=mid_row-1
            elif target>matrix[mid_row][n-1]:
                #target>matrix[mid_row][n-1]
                start_row=mid_row+1
        return False
