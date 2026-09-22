class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(row:int):
            nums=matrix[row]
            l,r=0,len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]>target:
                    r-=1
                else:
                    l+=1
            return False
            

        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            # which row the target could be in.
            if target<=matrix[i][n-1]:
                return search(i)
        return False
