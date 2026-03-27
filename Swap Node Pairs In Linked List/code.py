class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    node = Node(next = head)
    prev = node
    
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        
        first.next = second.next
        second.next = first
        prev.next = second
        
        prev = first
    return node.next
