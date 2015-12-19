class PrintableNodes:
  def __str__(self):
    current = self.head

    items = []

    while current != None:
      items.append(current.data)
      current = current.next

    return ','.join(str(item) for item in items)
