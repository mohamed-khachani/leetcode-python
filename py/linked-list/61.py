# Definition for singly-linked list.
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
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None or k == 0:
            return head

        length = 1
        last = head

        while last.next is not None:
            last = last.next
            length += 1

        k %= length

        if k == 0:
            return head

        last.next = head

        current = head
        for _ in range(length - k - 1):
            current = current.next

        new_head = current.next
        current.next = None

        return new_head



aa = Solution().rotateRight(generate_list([1,2,3,4,5]), 6)
print_graph(aa)