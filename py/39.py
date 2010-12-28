#!/usr/bin/python
import math


def get_pyt_triplet_c(a, b):
   c_sqr = a*a + b*b
   c = int(math.sqrt(c_sqr))
   if c_sqr % c != 0:
      return None
   
   return c


def num_triplets_with_abc_sum(target):
   limit = target
   result = 0
   for a in range(1, limit):
      for b in range(a, limit):
         c = get_pyt_triplet_c(a, b)
         if not c:
            continue
         if a+b+c == target:
            result += 1

   return result

max_solutions = 0
best_p = 0
for p in xrange(1,1000):
   num_solutions = num_triplets_with_abc_sum(p)
   if num_solutions > max_solutions:
      print "Found",num_solutions,"for p =",p
      max_solutions = num_solutions
      best_p = p

print "Result:", best_p
