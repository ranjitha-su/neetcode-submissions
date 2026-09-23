class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                print(stack)
                continue
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index=stack.pop()
                output[index]=i-index    
            stack.append(i)

        return output
            
        # [1,3,]
        # [1,-,1]