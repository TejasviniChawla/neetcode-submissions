class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s: 
            print(stack)
            if i in ['(', '{', '[']:
                stack.append(i)
            else: 
                if i==')':
                    if not stack or stack.pop()!='(':
                        return False
                elif i=='}':
                    if not stack or stack.pop()!='{':
                        return False
                elif i==']':
                    if not stack or stack.pop()!='[':
                        return False
                
        
        return not stack
                
        