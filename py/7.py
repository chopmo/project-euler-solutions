#!/usr/bin/python
from __future__ import with_statement
from timer import Timer
import math

def is_prime(k, known_primes):
   k_sqrt = math.ceil(math.sqrt(k))
   for x in known_primes:
      if k % x == 0:    return False
      elif x > k_sqrt:  return True
      
   return True


def nth_prime(n):
   primes = []
   x = 2
   while len(primes) < n:
      if is_prime(x, primes):
         primes.append(x)
         
      x += 1

   return primes[-1]

with Timer():
   print "Result: " + str(nth_prime(10001))
