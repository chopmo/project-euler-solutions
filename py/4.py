#!/usr/bin/python

import sys, time

def is_palindrome(n):
   s = str(n)
   for x in range(len(s)/2):
      if not s[x] == s[-(x+1)]:
         return False

   return True

def find_max_palin():
   x, y = 999, 999
   result = 0

   while x > 99:
      while y > 99:
         k = x * y
         if is_palindrome(k) and k > result:
            print "found new max: x=%i, y=%i, palindrome=%i" % (x,y,k)
            result = k
            
         y -= 1

      y = 999
      x -= 1
      
   return result


t0 = time.time()
maxpalin = find_max_palin()
t = time.time() - t0

print "Result: " + str(maxpalin)
print "It took %f secs." % t
