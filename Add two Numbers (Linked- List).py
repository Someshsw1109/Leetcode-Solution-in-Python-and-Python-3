class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # That's my 18th attempt.... w***
        
        Num1, Num2 = 0, 0
        while l1:
            Num1 = Num1 * 10 + l1.val
            l1 = l1.next
        
        while l2:
            Num2 = Num2 * 10 + l2.val
            l2 = l2.next
            
        Sum__ = Num1 + Num2
        curr = head = ListNode(0)
        
        if Sum__ == 0:
            return head
        while Sum__ > 0:
            head.next = ListNode(Sum__ % 10, head.next)
            Sum__ //= 10
        
        return curr.next

  # Follow me on instagram my insta id is - @codewithsomesh
