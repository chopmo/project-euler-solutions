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

def primes_less_than(max):
   primes = []
   k = 2
   while k < max:
      # Check known primes less than sqrt(k)
      if is_prime(k, primes):
         primes.append(k)

      k += 1

   return primes

def largest_prime_factor(num):
   num_sqrt = int(math.sqrt(num))
   primes = primes_less_than(num_sqrt)
   primes.reverse()
   for p in primes:
      if num % p == 0:
         return p

   return 0


with Timer():
   print "Result: %i" % largest_prime_factor(600851475143)

