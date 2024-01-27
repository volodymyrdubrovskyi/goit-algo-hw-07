from node_class_func import Node


def max_node_val(root: Node):
    current = root
    while current.right:
        current = current.right
    return current
