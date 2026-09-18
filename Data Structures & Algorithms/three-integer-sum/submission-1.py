class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(arr,target):
            hashset=set()
            twosum_output=[]
            for i in range(len(arr)):
                remaining=target-arr[i]
                if remaining in hashset:
                    twosum_output.append([remaining,arr[i]])
                hashset.add(arr[i])
            return twosum_output
        
        # nums.sort()
        # [-4,-1,-1,0,1,2]
        target=0
        output=set()
        for i in range(len(nums)):
            remaining_target=target-nums[i]
            # before=nums[:i]
            # after=nums[i+1:]
            remaining_nums=nums[:i]+nums[i+1:]
            twosum_result=twoSum(remaining_nums,remaining_target)
            for pair in twosum_result:
                triplet=tuple(sorted(pair+[nums[i]]))
                output.add(triplet)
                
        return [list(x) for x in output]

    