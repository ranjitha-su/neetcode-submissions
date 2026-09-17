from heapq import heappush, heappop
from math import inf
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        q=[]
        seq=[]
        for num in nums:
            heappush(q,num)
        
        prev=-inf
        longest_seq=0
        seq_length=0
        while q:
            cur_ele=heappop(q)
            if cur_ele==prev:
                continue
            if cur_ele-prev==1:
                seq_length+=1
            else:
                seq_length=1
            prev=cur_ele
            longest_seq=max(longest_seq,seq_length)
            
        return longest_seq