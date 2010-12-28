#!/usr/bin/env python

def digit_sum(n):
   return sum([int(x) for x in str(n)])

max_digit_sum = 0
for a in range(1,100):
   for b in range(1,100):
      max_digit_sum = max(max_digit_sum, digit_sum(a ** b))

print max_digit_sum

