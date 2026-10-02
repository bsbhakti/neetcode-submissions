class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            #print(stack)
            if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "/" or tokens[i] == "*":
                a = int(stack[-1])
                stack.pop()
                b = int(stack[-1])
                stack.pop()

                c = None
                if tokens[i] == "/":
                    c = int(b/a)
                    # #print("div", b//a, a//b)
                    # stack.append(c)
                elif tokens[i] == "+":
                    c = b+a
                elif tokens[i] == "-":
                    c = b-a
                else:
                    c = a *b 
                #print("popped",a,b,"res",c)
                stack.append(c)
            else:
                stack.append(int(tokens[i]))
        #print(stack)
        return stack[-1]


        