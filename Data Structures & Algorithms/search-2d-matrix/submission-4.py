class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(row:int):
            print(f"Search in row {row}")
            nums=matrix[row]
            l,r=0,len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return False
            

        m,n=len(matrix),len(matrix[0])
        l,r=0,m-1
        
        while l<=r:
            # which row the target could be in.
            mid=(l+r)//2
            # print(f"mid:{mid}")
            if matrix[mid][0]==target or matrix[mid][n-1]==target:
                return True
            if matrix[mid][0]<target<matrix[mid][n-1]:
                    return search(mid)
            elif target<matrix[mid][0]:
                # print(f"r={mid-1}")
                r=mid-1
            elif target>matrix[mid][n-1]:
                # print(f"l={mid+1}")
                l=mid+1
        return False
