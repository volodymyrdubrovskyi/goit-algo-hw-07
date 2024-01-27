from node_class_func import Node

def sum_node_val(node: Node):
    summa = node.val
    if node.left:
        summa += sum_node_val(node.left)
    if node.right:
        summa += sum_node_val(node.right)
    return summa