class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap:tuple[(char,int),[str]]={}
        output=[]
        for cur_str in strs:
            counter=Counter(cur_str)
            key=tuple(sorted(counter.items()))
            
        for cur_str in strs:
            counter=Counter(cur_str)
            key=tuple(sorted(counter.items()))
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(cur_str)
        
        # print(list(hashmap.values()))
        return list(hashmap.values())


