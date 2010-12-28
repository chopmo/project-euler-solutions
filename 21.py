from utils import *
from sets import Set

def d(n):
   return sum(get_divisors(n))

amicable_numbers = Set()

for a in range(1,10000):
   b = d(a)
   
   if d(b) == a and a != b:
      print "found",a,b
      amicable_numbers.add(a)
      amicable_numbers.add(b)

print sum(amicable_numbers)
