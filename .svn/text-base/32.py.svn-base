import sys
from decimal import Decimal
import math


def is_pandigital(a, b, x):
   digits = set()
   [digits.add(c) for c in str(a)]
   [digits.add(c) for c in str(b)]
   [digits.add(c) for c in str(x)]
   return len(digits) == 9 and (not '0' in digits)

numbers = set()

for a in range(1, 5000):
   for b in range(1, 10000):
      x = a * b
      if x > 9999:
         break

      if is_pandigital(a, b, x):
         # print "found", a, "*", b, "=", x
         numbers.add(x)

print sum(numbers)


