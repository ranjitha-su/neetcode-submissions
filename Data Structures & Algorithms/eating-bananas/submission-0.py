from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        hours=0
        k=0
        while l<=r:
            hours_for_this_pile=0
            mid=(l+r)//2
            for i in range(len(piles)):
                hours_for_this_pile+=ceil(piles[i]/mid)
            if hours_for_this_pile <= h:
                k=mid
                r=mid-1
            else:
                l=mid+1
        return k