class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap:tuple[(char,int),[str]]={}
        output=[]
        for cur_str in strs:
            counter=Counter(cur_str)
            key=tuple(sorted(counter.items()))
            hashmap[key]=[]
        for cur_str in strs:
            counter=Counter(cur_str)
            key=tuple(sorted(counter.items()))
            hashmap[key].append(cur_str)
        
        # print(list(hashmap.values()))
        return list(hashmap.values())


