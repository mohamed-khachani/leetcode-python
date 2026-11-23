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
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        
        new_head = head.next
        prev = None
        current = head

        while current is not None and current.next is not None:
            next_node = current.next
            nx = next_node.next

            # Swap los 2 nodes
            next_node.next = current
            current.next = nx

            if prev is not None:
                prev.next = next_node

            prev = current
            current = nx

        return new_head

aa = Solution().swapPairs(generate_list([1,2,3,4]))
print_graph(aa)