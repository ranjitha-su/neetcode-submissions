class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        cur_max=0
        while l<r:
            cur_max=max(cur_max, (r-l)*min(heights[l],heights[r]))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return cur_max