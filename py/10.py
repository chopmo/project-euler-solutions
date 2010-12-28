#!/usr/bin/python
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


print "Result: " + str(sum(primes_less_than(2000000)))

