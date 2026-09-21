class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                print(stack)
            else:
                # top=stack[-1]
                if temperatures[i] > temperatures[stack[-1]]:
                    while stack and temperatures[i] > temperatures[stack[-1]]:
                        top=stack[-1]
                        stack.pop()
                        output[top]=i-top
                    stack.append(i)     
                else:
                    stack.append(i)
        return output
        # 0. 1. 2. 3. 4. 5. 6. 
        # 30,38,30,29,25,40,28
        # stack=[]
        # output[1,4,3,2,1,0,0]