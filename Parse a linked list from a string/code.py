from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    str_list = list_repr.split('->')
    str_list = [s.strip() for s in str_list]
    node_values = str_list[:-1]
    
    cur_node = None
    for value in node_values[::-1]:
        cur_node = Node(int(value), cur_node)
    return cur_node
