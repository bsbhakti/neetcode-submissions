"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        prev = curr = prev_ret = head_ret = curr_ret = None
        curr = head
        my_map = {}
        while curr != None:
            # #print(my_map)
            if head_ret is None:
                head_ret = Node(head.val, None, None)
                curr_ret = head_ret
                my_map[head] = curr_ret
                
            else:
                if curr in my_map:
                    curr_ret = my_map[curr]
                else:
                    curr_ret = Node(curr.val,None, None)
                    my_map[curr] = curr_ret
            if prev_ret:
                    prev_ret.next = curr_ret
           
            if curr.random:
                    if curr.random in my_map:
                        # pop = my_set.pop(curr.random)
                        pop = my_map[curr.random]
                        curr_ret.random = pop
                    else:
                        new = Node(curr.random.val, None, None)
                        curr_ret.random = new
                        # my_set.add(new)
                        my_map[curr.random] = new
            # #print(/n/n/n/n)

            # if curr.random:
            #     #print("curr:",curr.val, curr, "curr.random", curr.random.val, "new curr:", curr_ret.val, curr_ret, "new curr random:", curr_ret.random.val, curr_ret.random)
            # else:
                #print("curr:",curr.val, curr, "new curr:", curr_ret.val, curr_ret)
            prev_ret = curr_ret
            curr_ret = None
            prev = curr
            curr = curr.next

        p = head_ret
        # while p != None:
        #     if(p.random):
        #         #print(p.random.val)
        #     p = p.next
        return head_ret
                 