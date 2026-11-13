class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        stack.append((0,temperatures[0]))
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            curr = temperatures[i]
            while len(stack) and stack[-1][1] < curr:
                pop = stack.pop()
                res[pop[0]] = i - pop[0]
            stack.append((i,curr))
        return res
        