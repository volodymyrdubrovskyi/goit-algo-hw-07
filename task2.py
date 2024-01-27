import node_class_func

def min_node_val(node: node_class_func.Node):
    current = node
    while current.left:
        current = current.left
    return current