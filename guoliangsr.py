from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
arr = [1, 2, 3, 4, 5, 6, 7, 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']

def buildTree(arr):
    i = 1
    root = TreeNode(arr[0])
    q = deque([root])
    while i < len(arr):
        node = q.popleft()
        if arr[i] != 'n':
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] != 'n':
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    
    return root

def preorder_traversal(root):
    if root is None:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)



root = buildTree(arr)
print(preorder_traversal(root))

print(inorder_traversal(root))