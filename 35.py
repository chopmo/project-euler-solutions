from utils import *
pg = PrimeGenerator()
pg.ensure_until(1000000)

def num_digits(number):
   return len(str(number))

def rotations(number):
   result = []
   for x in range(num_digits(number) - 1):
      number = int(str(number)[-1] + str(number)[0:-1])
      result.append(number)
      
   return result

def all_rotations_prime(prime):
   for rotated_prime in rotations(prime):
      if not pg.is_prime(rotated_prime):
         return False
      
   return True
   
result = 0
for prime in pg.primes:
   if all_rotations_prime(prime):
      result += 1

print "Result:", result
         
