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
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        current1, current2 = list1, list2
        l1, l2 = [], []

        while current1 is not None:
            l1.append(current1.val)
            current1 = current1.next

        while current2 is not None:
            l2.append(current2.val)
            current2 = current2.next

        l1.extend(l2)
        l1.sort()

        return generate_list(l1)

print_graph(Solution().mergeTwoLists(generate_list([]), generate_list([0])))