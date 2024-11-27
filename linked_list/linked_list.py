# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linklist(a):
    head = None
    next = None
    for i in range(len(a) - 1, -1, -1):
        if i == len(a) - 1:
            next = ListNode(a[i], None)
        else:
            head = ListNode(a[i], next)
            next = head
    return head

def build_linked_list_from_list(input_list):
    head = None
    tail = None
    for item in input_list:
        new_node = ListNode(item)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head



import math
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        tmp = head
        while tmp.next is not None:
            count += 1
            tmp = tmp.next
        i = 0
        new_head = head
        while head.next is not None:
            if i==math.floor(count/2)-1:
                new_next = head.next.next
                head.next = new_next
                break
            i += 1
            head = head.next
        return new_head

a = [1,2,3,4,5]
head = build_linklist(a)
b = Solution()
b.deleteMiddle(head)