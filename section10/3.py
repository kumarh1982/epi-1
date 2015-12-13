from lib.tree import BinaryTree

def lowest_common_ancestor(root, a, b):
  if root is None:
    return None

  if root == a or root == b:
    return root

  left  = lowest_common_ancestor(root.left, a, b)
  right = lowest_common_ancestor(root.right, a, b)

  if not left:  return right
  if not right: return left

  if (left == a and right == b) or (right == b and left == a):
    return root

tree = BinaryTree('4,10,12,14,15,16,20,21')
a    = tree.root.left.left
b    = tree.root.right.right

assert lowest_common_ancestor(tree.root, a, b).data == '14'
