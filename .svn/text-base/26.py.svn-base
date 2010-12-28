from decimal import *
import sys

getcontext().prec = 2000

def get_cycle_len(s):
   for cycle_len in range(2, 1000):
      if s[0:cycle_len] == s[cycle_len:cycle_len*2]:
         return cycle_len
         

# print get_cycle_len(str(Decimal(1) / Decimal(998))[10:])
# sys.exit(0)

max_cycle_len = 0
result = -1
for i in range(1, 1000):
   s = str(Decimal(1) / Decimal(i))

   # chop off the first bit to (hopefully) get to the cycling part
   chopped_s = s[10:]

   if len(chopped_s) == 0:
      continue
   
   cycle_len = get_cycle_len(chopped_s)
   if cycle_len > max_cycle_len:
      max_cycle_len = cycle_len
      result = i
      print "found cycle of len", cycle_len, "in i=", i

