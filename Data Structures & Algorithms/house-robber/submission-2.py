class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_or_skip(i: int):
            # term condition
            if i in memo:
                return memo[i]
            
            if i>=len(nums):
                return 0
            
            memo[i]=max(nums[i]+rob_or_skip(i+2), rob_or_skip(i+1))
            return memo[i]
        
        memo={}
        return rob_or_skip(0)
        #     Rob rob_or_skip(0)=nums[0]+rob_or_skip(2)
        #    skip rob_or_skip(0)=nums[1]+rob_or_skip(3)
        #    max(nums[0]+rob_or_skip(2), rob_or_skip(3))