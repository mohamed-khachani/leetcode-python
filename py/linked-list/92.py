# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_graph(head: ListNode | None):
    if head is None:
        print(None)
        return None
    current = head
    while current.next is not None:
        print(f'{current.val} -> ', end='')
        current = current.next
    print(current.val)

def generate_list(arr: list[int]):
    if len(arr) == 0:
        return None
    
    head = ListNode(arr[0])
    prev: ListNode = head

    for x in range(1, len(arr)):
        n = ListNode(arr[x])
        prev.next = n
        prev = n

    return head


class Solution:
    def reverse(self, head: ListNode, x: int) -> ListNode:
        arr = []
        i = 0
        current = head
        
        while i < x:
            i += 1
            arr.append(current)
            current = current.next

        for x in range(x-1, 0, -1):
            arr[x].next = arr[x-1]

        arr[0].next = current

        return arr[-1]
            

    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left == right or head is None:
            return head
        
        j = 0
        prev = None
        c = head
        while j < left-1:
            prev = c
            c = c.next
            j += 1
        
        start = self.reverse(c, right - left + 1)
        if prev is not None:
            prev.next = start
        else:
            head = start

        return head



aa = Solution().reverseBetween(generate_list([5]), 1,1)  # :) :)
print_graph(aa)