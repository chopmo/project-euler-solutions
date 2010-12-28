#!/usr/bin/python
from utils import *
from math import sqrt, floor
import sys

pg = PrimeGenerator()

# Annoyingly, I had to look up an algorithm for factoring:
# http://stackoverflow.com/questions/239865/best-way-to-find-all-factors-of-a-given-number-in-c
def find_num_factors(n): 
   # factors = []
   result = 0
   max = int(floor(sqrt(n)))
   for f in range(1, max + 1):
      if n % f == 0:
         # factors.append(f)
         result += 1
         d = n / f
         if d != f:
            # factors.append(d)
            result += 1

   # return factors
   return result

tri     = 6 # triangle number accumulator
tri_num = 3 # triangle number counter (1 is the first)

while True:
   if find_num_factors(tri) > 500:
      print "Result:", tri
      break

   # Generate the next triangle number
   tri_num += 1
   tri += tri_num
