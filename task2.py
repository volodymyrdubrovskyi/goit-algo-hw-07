from node_class_func import Node

def min_node_val(root: Node):
    current = root
    while current.left:
        current = current.left
    return current