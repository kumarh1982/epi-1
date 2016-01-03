from lib.tree import BinaryTree

def height(node):
  height = 0

  while node.parent is not None:
    node = node.parent

  return height

def lowest_common_ancestor(node1, node2):
  h1, h2 = height(node1), height(node2)

  if h1 > h2:
    h1,    h2    = h2,    h1
    node1, node2 = node2, node1

  for _ in range(h2 - h1):
    node2 = node2.parent

  while node1 is not node2:
    node1 = node1.parent
    node2 = node2.parent

  return node1

tree = BinaryTree('4,10,12,14,15,16,20,21')
a    = tree.root.left.left
b    = tree.root.right.right

assert lowest_common_ancestor(a, b).data == '14'
