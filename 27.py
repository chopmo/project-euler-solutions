from utils import *
import sys

pg = PrimeGenerator()

def num_consec_primes(a, b):
   n = 0
   while True:
      k = n ** 2 + a * n + b
      pg.ensure_until(k)
      if not pg.is_prime(k):
         return n

      n += 1

# print num_consec_primes(1, 41)
# sys.exit(0)

max_n = 0

for a in range(-999, 1000):
   for b in range(-999, 1000):
      num_n = num_consec_primes(a,b)
      if num_n > max_n:
         max_n = num_n
         print "Found new max: a =",a,", b =",b, "num_n =",num_n,"res =", a*b
