'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    

class Solution:
    def add_two_numbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p = l1
        q = l2
        curr = dummyHead
        carry = 0
        
        while (p != None or q != None):
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            summed = carry + x + y
            carry = summed // 10
            curr.next = ListNode(summed % 10)
            curr = curr.next
            if (p != None):
                p = p.next
            if (q != None):
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummyHead.next