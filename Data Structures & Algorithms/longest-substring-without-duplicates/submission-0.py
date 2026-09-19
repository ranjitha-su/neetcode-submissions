class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        longest=0
        exists=set()
        while r<len(s):
            if s[r] not in exists:
                exists.add(s[r])
                r+=1
            else:
                longest=max(longest,len(exists))
                while s[r] in exists:
                    exists.remove(s[l])
                    l+=1
        longest=max(longest,len(exists))
        return longest
#   l    r
# abcbdef

# exists={c,b,d,e,f}