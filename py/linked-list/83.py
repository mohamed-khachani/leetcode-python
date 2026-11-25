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
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current = head

        while current is not None:
            if current.next is not None and current.next.val == current.val:
                duplicate = current.val
                c = current

                while c is not None and c.val == duplicate:
                    c = c.next

                current.next = c
            else:
                current = current.next

        return head



aa = Solution().deleteDuplicates(generate_list([1,1,2,3,3])) # :)
print_graph(aa)