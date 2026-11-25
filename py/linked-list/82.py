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
        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current is not None:
            if current.next is not None and current.val == current.next.val:
                duplicate = current.val

                while current is not None and current.val == duplicate:
                    current = current.next

                prev.next = current

            else:
                prev = current
                current = current.next

        return dummy.next



aa = Solution().deleteDuplicates(generate_list([1,1,1,2,3]))
print_graph(aa)