import operator

class Heap:
  def __init__(self, data=[]):
    self.data = data

  def __str__(self):
    return ','.join(str(item) for item in self.data)

  @staticmethod
  def build(data):
    heap = Heap()
    for item in data:
      heap.insert(item)

    return heap

  def peek(self):
    if self.data:
      return self.data[0]

  def pop(self):
    if not self.data:
      return

    top    = self.data[0]
    last_i = self.size() - 1

    self.swap(0, last_i)
    self.data.pop()
    self.bubble_down()

    return top

  def insert(self, item):
    self.data.append(item)
    self.bubble_up();

    return item

  def size(self):
    return len(self.data)

  def bubble_down(self):
    current_index = 0

    while True:
      left_index  = (current_index * 2) + 1
      right_index = (current_index * 2) + 2

      # The case where there are no children.
      if left_index > self.size() - 1:
        break

      # The case where there is one child.
      if right_index > self.size() - 1:
        self.swap_greater(left_index, current_index)
        break

      larger = max(left_index, right_index, key=lambda a: self.data[a])
      if self.data[larger] <= self.data[current_index]:
        break

      self.swap(current_index, larger)

  def bubble_up(self):
    current_index = self.size() - 1

    while True:
      parent_index = (current_index - 1) // 2

      if parent_index < 0:
        break

      if self.data[parent_index] >= self.data[current_index]:
        break

      self.swap_lesser(parent_index, current_index)
      current_index = parent_index

  def swap(self, i, j):
    self.data[i], self.data[j] = self.data[j], self.data[i]

  def try_swap(self, i, j, operator):
    if operator(self.data[i], self.data[j]):
      self.swap(i, j)

  def swap_greater(self, i, j):
    self.try_swap(i, j, operator.gt)

  def swap_lesser(self, i, j):
    self.try_swap(i, j, operator.lt)

def test_heap(heap):
  assert heap.pop() == 9
  assert heap.pop() == 6
  assert heap.pop() == 5
  assert heap.pop() == 4
  assert heap.pop() == 3
  assert heap.pop() == 1
  assert heap.pop() is None

if __name__ == '__main__':
  test_heap(Heap([9,5,6,1,3,4]))
  test_heap(Heap.build([1,6,9,4,5,3]))
