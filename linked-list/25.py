# Definition for singly-linked list.
from time import sleep
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
        # sleep(1)
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

# ---- # 
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or k == 1:
            return head

        current = head
        nodes = []
        nodes_prev = None
        new_head = head

        while current is not None:
            next_node = current.next
            nodes.append(current)

            if len(nodes) == k:
                for i in range(k-1, 0, -1):
                    nodes[i].next = nodes[i-1]
                
                
                if nodes_prev is not None:
                    nodes_prev.next = nodes[-1]
                else:
                    new_head = nodes[-1]

                nodes_prev = nodes[0]
                nodes_prev.next = None
                nodes.clear()

            current = next_node

        if nodes_prev is not None:
            nodes_prev.next = nodes[0] if nodes else None

        return new_head

        

aa = Solution().reverseKGroup(generate_list([1,2,3,4,5]), 3)
print_graph(aa)