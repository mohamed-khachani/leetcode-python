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



# class Solution:
#     def partition(self, head: ListNode | None, x: int) -> ListNode | None:
#         p1: list[ListNode]= []
#         p2: list[ListNode] = []
#         current: ListNode = head

#         while current is not None:
#             if current.val < x:
#                 p1.append(current)
#             else:
#                 p2.append(current)
#             current = current.next

#         for i in range(len(p1)-1):
#             p1[i].next = p1[i+1]

#         p1[-1].next = p2[0]

#         for j in range(len(p2)-1):
#             p2[j].next = p2[j+1]

#         p2[-1].next = None

#         return p1[0]


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        if head is None:
            return None
        
        head1: ListNode | None = None
        head2: ListNode | None = None
        first_head_1: ListNode | None = None
        first_head_2: ListNode | None = None
        current: ListNode = head

        while current is not None:
            if current.val < x:
                if head1 is not None:
                    head1.next = current
                    head1 = current
                else:
                    head1 = current
                    first_head_1 = current
            else:
                if head2 is not None:
                    head2.next = current
                    head2 = current
                else:
                    head2 = current
                    first_head_2 = current
                
            current = current.next

        if head1 is not None:
            head1.next = first_head_2

        if head2 is not None:
            head2.next = None
        
        return first_head_1 if first_head_1 is not None else first_head_2


aa = Solution().partition(generate_list([1,4,3,2,5,2]), 2)  # :) :)
print_graph(aa)