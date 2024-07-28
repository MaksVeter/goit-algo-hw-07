class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def find_max(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.value


def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.value



def sum_values(root):
    if root is None:
        return 0
    return root.value + sum_values(root.left) + sum_values(root.right)

# test
root = TreeNode(20)
root = insert(root, 10)
root = insert(root, 30)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 25)
root = insert(root, 35)

print("Max:", find_max(root))
print("Min:", find_min(root))
print("Sum:", sum_values(root))
