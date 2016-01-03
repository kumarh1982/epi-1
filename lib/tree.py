class Node:
  def __init__(self, data=None, left=None, right=None, parent=None):
    self.left   = left
    self.right  = right
    self.data   = data
    self.parent = parent

class BinaryTree:
  def __init__(self, data):
    """
    `data` is a string representing an inorder traversal. E.g. `1,6,5,3,4`
    """

    self.root = self.parse_tree(data.split(','))

  def __str__(self):
    return ','.join(map(str, list(self.inorder(self.root))))

  def inorder(self, node):
    if node is None:
      return

    for elem in self.inorder(node.left): yield elem
    yield node.data
    for elem in self.inorder(node.right): yield elem

  def parse_tree(self, data, left=None, right=None, parent=None):
    if left is None:
      left = 0

    if right is None:
      right = len(data) - 1

    if left > right:
      return

    middle = (left + right) // 2

    root       = Node(data[middle])
    root.left  = self.parse_tree(data, left, middle - 1, root)
    root.right = self.parse_tree(data, middle + 1, right, root)

    if parent:
      root.parent = parent

    return root

if __name__ == '__main__':
  tree = BinaryTree('1,6,5,3,4')
  assert tree.__str__() == '1,6,5,3,4'
