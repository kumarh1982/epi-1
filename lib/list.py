from lib.printable import PrintableNodes

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class List(PrintableNodes):
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def is_empty(self):
    return self.head is None

  def find(self, value):
    current = self.head

    while current:
      if (callable(value) and value(current.data)) or (current.data == value):
        return current

      current = current.next

  def add(self, data):
    self.size += 1

    new_node = Node(data)

    if self.is_empty():
      self.head = new_node
      self.tail = self.head
      return self.head

    self.tail.next = new_node
    self.tail = new_node
    return data

  def remove(self, value):
    """
    Removes an item from the list. Assumes unique data values.
    """

    previous = None
    current  = self.head

    while current:

      if (callable(value) and value(current.data)) or (current.data == value):
        if previous:
          previous.next = current.next

          if not current.next:
            self.tail = previous

        else:
          self.head = current.next

          if not current.next:
            self.tail = None

        self.size -= 1
        return current

      previous = current
      current  = current.next

if __name__ == '__main__':
  items = List()
  items.add(1)
  items.add(2)
  items.add(3)
  items.remove(2)
  items.add(4)
  items.remove(1)
  items.remove(2)
  items.remove(3)
  items.remove(4)
  items.remove(5)
  items.remove(6)

  assert str(items) == ''
  assert items.size == 0
