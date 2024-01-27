from node_class_func import Node

def sum_node_val(root: Node):
    summa = root.val
    if root.left:
        summa += sum_node_val(root.left)
    if root.right:
        summa += sum_node_val(root.right)
    return summa