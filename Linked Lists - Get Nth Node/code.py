class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None or index < 0:
        raise Exception('Error')
    else:
        cur = node
        counter = 0
        while cur is not None:
            if counter == index:
                return cur
            else:
                cur = cur.next
                counter += 1
        else: raise Exception('Out of range')
