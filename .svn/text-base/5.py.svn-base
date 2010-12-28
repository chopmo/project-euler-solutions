#!/usr/bin/python
from __future__ import with_statement
from timer import Timer

def is_evenly_divisible_by_all_in(k, numbers):
   for x in numbers:
      if k % x != 0:
         return False

   return True   

def smallest_evenly_divisible_by_all(numbers):
   k = 20
   while True:
      if is_evenly_divisible_by_all_in(k, numbers):
         return k

      k += 20


numbers = range(1,21)
numbers.reverse() # Should be faster...?

with Timer():
   result = smallest_evenly_divisible_by_all(numbers)
   
print "Result: " + str(result)
