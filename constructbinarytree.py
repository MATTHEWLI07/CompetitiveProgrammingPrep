preOrder=[1,2,4,8,5,3,6,7]
inOrder=[8,4,2,5,1,6,3,7]

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None




def build_tree(root, pre_order, left_or_right, sub_tree):
    if(sub_tree == []):
        return
    node = TreeNode(pre_order[0])
    if(left_or_right == 'l'):
        root.left = node
    else:
        root.right = node
    try:
        index = sub_tree.index(pre_order[0])
       
    except ValueError:
        return

    subleft_tree = sub_tree[0:index]
    build_tree(node,  pre_order[1:], 'l', subleft_tree)
    subright_tree = sub_tree[index + 1:]
    build_tree(node,  pre_order[index + 1:], 'r', subright_tree)
    
    return

def preorder_traversal(root):
    if root is None:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


root = TreeNode(preOrder[0])
index = inOrder.index(preOrder[0])
build_tree(root,  preOrder[1:], 'l', inOrder[0:index] )
build_tree(root,  preOrder[index + 1:], 'r', inOrder[index + 1:] )




print(preorder_traversal(root))

print(inorder_traversal(root))