from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_so_far=inf
        max_profit=0
        for i in range(len(prices)):
            if i>0:
                max_profit=max(max_profit,prices[i]-minimum_so_far)
            minimum_so_far=min(minimum_so_far, prices[i])
        return max_profit