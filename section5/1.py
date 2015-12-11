import random

"""
5.1 Computing the parity of a word

The parity of a binary word is 1 if the number of 1s in the word is odd;
otherwise, it is 0. For example, the parity of 1011 is 1, and the parity of
10001000 is 0. Parity checks are used to detect single bit errors in data
storage and communication. It is fairly straightforward to write code that
computes the parity of a single 64-bit word.

How would you compute the parity of a very large number of 64-bit words?
"""

def make_popcount_function():
  table = [0]
  for index in range(1, 2**16):
    table.append(table[index >> 1] + (index & 1))

  def popcount(word):
    return table[(word >> 48) & 0xffff] + \
           table[(word >> 32) & 0xffff] + \
           table[(word >> 16) & 0xffff] + \
           table[(word) & 0xffff]

  return popcount

popcount = make_popcount_function()

def parity(word):
  return popcount(word) % 2

def test():
  assert popcount(0b1001011000111000011000000000000000111000000000000011000000000001) == 15
  assert   parity(0b1001011000111000011000000000000000111000000000000011000000000001) == 1

  for _ in range(2**16):
    parity(random.getrandbits(64))

test()
