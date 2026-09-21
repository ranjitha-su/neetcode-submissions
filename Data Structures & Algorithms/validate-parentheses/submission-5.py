class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i] in ['[', '{', '(']:
                stack.append(s[i])
            else:
                if stack:
                    popped=stack.pop()
                    print(f"popped: {popped} s[i]:{s[i]}")
                    if (s[i]==']' and popped in ['{', '(']) or \
                        (s[i]=='}' and popped in ['[', '(']) or \
                        (s[i]==')' and popped in ['{', '[']):
                        return False
                else:
                    return False
        return len(stack)==0