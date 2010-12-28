#!/usr/bin/python
import math

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.  Find the
# product abc.


def get_pyt_triplet_c(a, b):
   c_sqr = a*a + b*b
   c = int(math.sqrt(c_sqr))
   if c_sqr % c != 0:
      return None
   
   return c


def get_py_triplet_with_abc_sum(target):
   # limit = int(math.ceil(math.sqrt(target)))  # XXX: Is this OK?
   limit = target
   for a in range(1, limit):
      for b in range(a, limit):
         c = get_pyt_triplet_c(a, b)
         if not c:
            continue
         if a+b+c == target:
            return (a, b, c)

t = get_py_triplet_with_abc_sum(1000)

print "Result: " + str(t[0] * t[1] * t[2])
