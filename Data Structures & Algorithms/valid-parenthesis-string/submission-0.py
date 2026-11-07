class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_l = []
        stack_s = []

        for j in range(len(s)):
            i = s[j]
            if i == "(":
                stack_l.append(j)
            elif i == "*":
                stack_s.append(j)
            else:
                if len(stack_l):
                    stack_l.pop()
                elif len(stack_s):
                    stack_s.pop()
                else:
                    return False
        while stack_l:
            # print(stack_s, stack_l)
            if len(stack_s):
                while len(stack_s) and stack_s[-1] < stack_l[-1]:
                    stack_s.pop()
                if len(stack_s) == 0 and len(stack_l) == 0:
                    return True
                elif len(stack_s) == 0:
                    return False 
                stack_l.pop()
                stack_s.pop()
            
            else:
                
                return False
        return True
                
                

        