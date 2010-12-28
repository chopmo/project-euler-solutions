from bisect import bisect_left
from utils import *

def is_abundant(number):
   return sum(get_proper_divisors(number)) > number

limit = 28123
abundant_numbers = []

# Find all relevant abundant numbers
for i in range(limit):
   if is_abundant(i):
      abundant_numbers.append(i)

print "found", len(abundant_numbers), "abundant numbers"

def is_composable(number):
   for a1 in abundant_numbers:
      if a1 >= number:
         return False

      a2 = number - a1
      
      if abundant_numbers[bisect_left(abundant_numbers, a2)] == a2:
         return True

   return False

# Find all numbers that cannot be written as the sum of two abundant numbers.
numbers = []
for i in range(1, limit):
   if i % 10000 == 0:
      print "looking at", i
      
   if not is_composable(i):
      # print "found", i
      numbers.append(i)

import pdb; pdb.set_trace() # __PYDEBUG__
print "Result:", sum(numbers)
