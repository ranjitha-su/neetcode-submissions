class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(l, r):
            print(f"bin_search({l}, {r})")
            while l<=r:
                mid=(l+r)//2
                print(f"mid: {mid}")
                if target==nums[mid]:
                    print(f"nums_slice[{mid}]:{nums[mid]}")
                    return mid
                elif target > nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            return -1
        
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid] < nums[r]:
                r=mid
        pivot_index=l
        
        if target==nums[pivot_index]:
            return pivot_index
        print("search right half")
        result = bin_search(pivot_index, len(nums)-1)
        if result == -1:
            print("Search in left half")
            result = bin_search(0, pivot_index)
        return result