#2 Add two numbers
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2: ListNode) -> ListNode:
        vals1 = []
        vals2 = []
        list1 = l1
        list2 = l2
        while list1 is not None:
            vals1.append(list1.val)
            list1 = list1.next
        while list2 is not None:
            vals2.append(list2.val)
            list2 = list2.next            
        val1 = ''   
        val2 = ''
        for i in vals1:
            val1+= str(i)
        for i in vals2:
            val2+= str(i)
        result = int(val1[::-1]) + int(val2[::-1])
        res = [int(x) for x in str(result)[::-1]]
        c = ListNode(res[0])
        ll = c
        temp4 = c
        for i in range(1, len(res)):
            newnode = ListNode(res[i])
            ll.next = newnode
            ll = ll.next
        return temp4
