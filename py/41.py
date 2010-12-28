from utils import *

pg = PrimeGenerator()
max_result = 0
p = 0
while p < 1000000000:
   pg.generate_next_prime()
   p = pg.primes[-1]
   if is_pandigital(p):
      max_result = p
      print p
      
# Doesn't terminate within a reasonable amount of time...result is where it seems stuck ;-)
