class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        coins.sort()
        cache = {}
        if amount == 0:
            return 1
        def recur(left,ind):
            # print(ind, left)

            if ind >= len(coins):
                return 0
            elif left == 0:
                return 1
            elif (ind,left) in cache:
                return cache[(ind,left)]
            c = 0
            for i in range(ind, len(coins)):
                if coins[i] > left:
                    break
                a = recur(left-coins[i], i)   
                if a != 0:
                    c+=a
                    # print(coins[i])
            cache[(ind,left)] = c
            # if left == amount:
            #     res += c

            return c

        return recur(amount, 0)
        # r = 0
        # print(cache)
        # for i in cache:
        #     # print(i)
        #     if i[1] == amount:
        #         # print(cache[i])
        #         r += cache[i]
        # print("res", res)
        return res               

        