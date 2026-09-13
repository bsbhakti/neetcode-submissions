# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # prev = None
        # curr = head

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        # if n==1:
        #     prev = prev.next
        #     return prev
        # else:        
        #     count = 2
        #     before = prev
        #     print(prev.val)
        #     prev = before.next
        #     newhead = before
            
        #     while before and prev:
        #         if count==n:
        #             temp= prev.next
        #             before.next = temp
        #         print(prev.val)
        #         prev = prev.next
        #         before = before.next
        #         count +=1

        #         prev = None
        #         curr = newhead

        #         while curr:
        #             temp = curr.next
        #             curr.next = prev
        #             prev = curr
        #             curr = temp

        #         return prev
        dummy, dummy.next = ListNode(), head
        left = dummy
        right = head

        if(n > 0):
            for i in range(n):
                print("d")
                right = right.next
        # print(right.val)

        while right:
            right = right.next
            left = left.next

        print(left.val)
        temp = left.next.next
        left.next = temp
        
        # while left:
        #     print(left.val)
        #     left = left.next
        return dummy.next
        


        