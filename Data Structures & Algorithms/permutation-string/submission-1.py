class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isPermutation(str1: str, str2: str) -> bool:
            return Counter(str1) == Counter(str2)
            
        l,r=0,1
        while r<=len(s2):
            win_len=len(s2[l:r])
            if win_len < len(s1):
                r+=1
                continue
            if win_len == len(s1):
                window=s2[l:r]
                if isPermutation(window, s1):
                    return True
                else:
                    l+=1
        return False