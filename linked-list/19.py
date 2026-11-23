from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def generate_list(arr: list[int]):
    head = ListNode(arr[0])
    prev: ListNode = head

    for x in range(1, len(arr)):
        n = ListNode(arr[x])
        prev.next = n
        prev = n

    return head

def print_graph(head: ListNode | None):
    if head is None:
        print(None)
        return None
    current = head
    while current.next is not None:
        print(f'{current.val} -> ', end='')
        current = current.next
    print(current.val)

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        lista: list[ListNode] = []
        current = head
        while current.next is not None:
            lista.append(current)
            current = current.next
        lista.append(current)

        if len(lista) == 1 and n == 1:
            return None

        if len(lista) == n:
            return lista[1]

        if n > len(lista):
            return head

        if 0 <= len(lista)-n-1 < len(lista) :
            lista[-n-1].next = lista[-n+1] if len(lista)-n+1 < len(lista) else None

        return head


print_graph(Solution().removeNthFromEnd(generate_list([1,2,3,4,5]), 16)) # :)