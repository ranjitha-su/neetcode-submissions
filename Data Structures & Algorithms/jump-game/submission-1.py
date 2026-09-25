class Solution:
    def canJump(self, nums: List[int]) -> bool:
        longest_jump,i,last_index=0,0,len(nums)-1
        while i<=longest_jump:
            longest_jump=max(longest_jump, i+nums[i])
            print(longest_jump)
            if longest_jump >=last_index:
                return True
            i+=1
        return False