from avl_tree import *

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
    current = node
    pass

# Задаю дерево
root = 0
keys = [10, 20, 31, 25, 28, 27, -2, 110]

for key in keys:
    root = insert(root, key)
    # print(root)

print("Найменший елемент:", find_min(root))
print("Найбільший елемент:", find_max(root))