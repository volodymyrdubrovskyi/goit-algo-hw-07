import node_class_func

def max_node_val(root: node_class_func.Node):
    current = root
    while current.right:
        current = current.right
    return current

def main():
    root = node_class_func.Node(5)
    root = node_class_func.insert(root, 3)
    root = node_class_func.insert(root, 2)
    root = node_class_func.insert(root, 4)
    root = node_class_func.insert(root, 7)
    root = node_class_func.insert(root, 6)
    root = node_class_func.insert(root, 8)

    #print(root)

    print(max_node_val(root))

if __name__ == '__main__':
    main()