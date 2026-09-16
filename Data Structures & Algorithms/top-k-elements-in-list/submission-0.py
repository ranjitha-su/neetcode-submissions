from collections import Counter
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        q=[]
        output=[]
        for key,val in counter.items():
            # k - element
            # v = count of the element.
            heappush(q,(-1*val,key))
        for i in range(k):
            value, key=heappop(q)
            output.append(key)
        return output