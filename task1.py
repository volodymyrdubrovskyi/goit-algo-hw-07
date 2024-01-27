import node_class_func

def max_node_val(root: node_class_func.Node):
    current = root
    while current.right:
        current = current.right
    return current
