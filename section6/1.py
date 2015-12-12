"""
6.1 Write a program that takes an array A and an index i into A, and rearranges
the elements such that all elements less than A[i] (the “pivot”) appear first,
followed by elements equal to the pivot, followed by elements greater than the
pivot.

Hint: Think about the partition step in quicksort.
"""

def swap(items, a, b):
  items[a], items[b] = items[b], items[a]

def partition1(items, pivot):
  """
  First attempt at a solution First we create a partition of elements less than
  pivot and elements greater than or equal to pivot. Then we further divide the
  second partition into elements equal to pivot and elements greater than pivot.
  """

  def swap_and_move(items, condition, left=None, right=None):
    if not left:
      left = 0

    if not right:
      right = len(items) - 1

    while left < right:
      if condition(items[left]) and not condition(items[right]):
        swap(items, left, right)

      if condition(items[right]):    right -= 1
      if not condition(items[left]): left += 1

    return left

  left = swap_and_move(items, lambda a: a >= pivot)
  left = swap_and_move(items, lambda a: a != pivot, left)

  return items

def partition2(items, pivot):
  """
  Converted to Python from solution in book.
  """

  smaller = 0
  equal   = 0
  larger  = len(items)

  while equal < larger:
    if items[equal] < pivot:
      swap(items, smaller, equal)
      smaller += 1
      equal += 1

    elif items[equal] == pivot:
      equal += 1

    # items[equal] > pivot
    else:
      larger -= 1
      swap(items, equal, larger)

  return items

def validate(items, pivot):
  smaller = set(elem for elem in items if elem < pivot)
  equal   = set(elem for elem in items if elem == pivot)
  larger  = set(elem for elem in items if elem > pivot)

  current = 'smaller'
  for item in items:
    if current == 'smaller':
      if item in larger:  return False
      if item in equal:   current = 'equal'
    elif current == 'equal':
      if item in smaller: return False
      if item in larger:  current = 'larger'
    elif current == 'larger':
      if item in smaller: return False
      if item in equal:   return False

  return True

def test():
  items = [4, 10, -5, 2, 1, 9, 6, 5, 5, 4, -40, 3, 4]
  assert validate(partition1(items, 5), 5)
  assert validate(partition2(items, 5), 5)

test()
