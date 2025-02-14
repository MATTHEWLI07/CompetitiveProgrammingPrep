from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))

#preorder = [3, 9, 20, 15, 7]
#inorder = [9, 3, 15, 20, 7]

inorder_map = defaultdict()
for i in range(len(inorder)):
    inorder_map[inorder[i]] = i
    
preorder_idx = 0

def build_tree(inorder_start, inorder_end):
    global preorder_idx
    if inorder_start > inorder_end:
        return
    
    root_val = preorder[preorder_idx]
    root = TreeNode(root_val)
    preorder_idx += 1
    root_idx = inorder_map[root_val]
    root.left = build_tree(inorder_start, root_idx - 1)
    root.right = build_tree(root_idx + 1, inorder_end)
    
    return root


def print_tree(root):
    if root == None:
        return []

    return [root.val] + print_tree(root.left) + print_tree(root.right)

root = build_tree(0, len(inorder) - 1)

res = print_tree(root)

print(res)
    

        
    
        
        
        
        
