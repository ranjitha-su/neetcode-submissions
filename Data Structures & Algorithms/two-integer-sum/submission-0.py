class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}       
        for i in range(len(nums)):
            remaining_target=target-nums[i]
            if remaining_target in nums_map:
                return sorted([i,nums_map[remaining_target]])
            else:
                nums_map[nums[i]]=i

        
       