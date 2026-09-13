class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for bracket in s:
            if(bracket not in Map):
                stack.append(bracket)
                continue
            if(not stack or stack[-1] != Map[bracket]):
                return False
            stack.pop()
        return not stack
        
