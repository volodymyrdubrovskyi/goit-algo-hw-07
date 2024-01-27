import node_class_func

def sum_node_val(node: node_class_func.Node):
    summa = node.val
    if node.left:
        summa += sum_node_val(node.left)
    if node.right:
        summa += sum_node_val(node.right)
    return summa