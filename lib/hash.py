from lib.list import List

class Hash:
  # `BUCKETS` and `MULTIPLIER` are coprime to help reduce collisions.
  BUCKETS    = 499
  MULTIPLIER = 11

  def __init__(self):
    self.buckets = [List()] * self.BUCKETS

  def __getitem__(self, key):
    node = self.buckets[self._hash(key)].find(lambda pair: pair[0] == key)
    if node is not None:
      return node.data[1]

  def __setitem__(self, key, value):
    self.buckets[self._hash(key)].add((key, value))

  def __delitem__(self, key):
    self.buckets[self._hash(key)].remove(lambda pair: pair[0] == key)

  def _exp(self, pair):
    return ord(pair[1]) * (self.MULTIPLIER ** pair[0])

  def _hash(self, key):
    return sum(map(self._exp, enumerate(str(key), start=1))) % self.BUCKETS

if __name__ == '__main__':
  h = Hash()
  h['hello'] = 'world'
  h['foo']   = 'bar'
  h['bar']   = 'baz'

  del h['bar']

  assert h['hello'] == 'world'
  assert h['foo']   == 'bar'
  assert h['bar']   is None
