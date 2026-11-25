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
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        l = []

        for k in range(len(lists)):
            current = lists[k]
            while current is not None:
                l.append(current.val)
                current = current.next

        l.sort()
        return generate_list(l)

arr = [[]]
inp = []
for x in arr:
    inp.append(generate_list(x))

print_graph(Solution().mergeKLists(inp)) # :)