class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        # value:index
        
        for i in range(len(numbers)):
            remaining_target=target-numbers[i]
            if remaining_target in hashmap:
                return [hashmap[remaining_target], i+1]
            hashmap[numbers[i]]=i+1

        