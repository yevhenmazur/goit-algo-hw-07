from avl_tree import insert

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key

def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.key

def find_sum(node):
    if node is None:
        return 0
    return node.key + find_sum(node.left) + find_sum(node.right)

# Задаю дерево
root = 0
keys = [10, 20, 31, 25, 28, 27, -2, 111]

for key in keys:
    root = insert(root, key)
    # print(root)

print("Найменший елемент:", find_min(root))
print("Найбільший елемент:", find_max(root))
print("Сума:", find_sum(root))
