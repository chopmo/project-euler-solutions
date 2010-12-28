from math import floor, sqrt

class PrimeGenerator:
   def __init__(self):
      self.primes = [2, 3]

   def generate_next_prime(self):
      n = self.primes[-1] + 2
      while not self.is_prime(n):
         n += 2

      self.primes.append(n)

   # Check if n is prime (given our currently known primes)
   def is_prime(self, n):
      if n < 2:
         return False
      
      for x in self.primes:
         if n == x:
            return True
         elif n % x == 0:
            return False
         elif x*x > n:
            break
         
      return True

   # Ensure that a prime larger than or equal to n has been generated
   def ensure_until(self, n):
      while self.primes[-1] < n:
         self.generate_next_prime()

class TriangleNumberGenerator:
   def __init__(self):
      self.triangle_numbers = [1]
      self.max_num = 0

   def __triangle_number(self, n):
      return n * (n+1) / 2
   def __generate_next(self):
      self.max_num += 1
      self.triangle_numbers.append(self.__triangle_number(self.max_num))

   def __ensure_until(self, n):
      while self.triangle_numbers[-1] < n:
         self.__generate_next()

   def is_triangle_number(self, n):
      self.__ensure_until(n)
      return n in self.triangle_numbers
   

def get_proper_divisors(n):
   factors = []
   max = int(floor(sqrt(n)))
   for f in range(1, max + 1):
      if n % f == 0:
         factors.append(f)
         if f == 1:
            continue
         
         d = n / f
         if d != f:
            factors.append(d)

   return factors

# XXX: Delete?
def get_divisors(n):
   result = []
   for i in range(1, n):
      if n % i == 0:
         result.append(i)

   return result

def is_pandigital(i):
   s = str(i)
   for i in range(len(s)):
      if not str(i+1) in s:
         return False
   return True


def fact(n):
   if n == 0:
      return 1
   else:
      return n == 1 and 1 or n * fact(n - 1)

def num_digits(number):
   return len(str(number))
