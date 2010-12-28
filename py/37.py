from utils import *
import sys

# Find the sum of the only eleven primes that are both truncatable from left to right and
# right to left.
pg = PrimeGenerator()

num_truncatable_primes = 11
found_primes = 0

def is_truncatable_prime(prime):
   s = str(prime)
   p_len = len(s)
   for i in range(1, p_len):
#       print s
#       print s[0:i]
#       print s[i:p_len]
      
      if not pg.is_prime(int(s[0:i])):
         return False
      if not pg.is_prime(int(s[i:p_len])):
         return False
      
   return True

result = 0
while found_primes < num_truncatable_primes:
   pg.generate_next_prime()
   prime = pg.primes[-1]
   
   if prime < 10:
      continue

   if is_truncatable_prime(prime):
      print "Found", prime
      result += prime
      found_primes += 1

print "Result:", result
