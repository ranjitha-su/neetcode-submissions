from heapq import heappush,heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        s_counter=Counter(s)
        prev=None
        path=[]
        q=[]
        for key,value in s_counter.items():
            heappush(q,(-1*value, key))
        
        while q:
            # pop the max count element(least *-1)
            value,key=heappop(q)
            if prev==(value,key):
                # pop again
                if not q:
                    return ""
                value,key=heappop(q)
                heappush(q,prev)

            path.append(key)
            value+=1
            prev=value,key
            if value<0:
                heappush(q,prev)
        return "".join(path)
