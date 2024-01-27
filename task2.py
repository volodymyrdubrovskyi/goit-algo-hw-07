from node_class_func import Node

def min_node_val(node: Node):
    current = node
    while current.left:
        current = current.left
    return current