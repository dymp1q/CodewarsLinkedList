class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    cur_node = node
    nodes = []
    while cur_node:
        nodes.append(str(cur_node.data))
        nodes.append(' -> ')
        cur_node = cur_node.next
    
    nodes.append('None')
    return ''.join(nodes)
