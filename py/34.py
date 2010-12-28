import math

def fact(x):
   result = 1
   while x > 1:
      result *= x
      x -= 1

   return result

x = 3
result = 0
while True:
   digit_fact_sum = sum([fact(int(digit)) for digit in str(x)])
   if digit_fact_sum == x:
      print "found", x
      result += x

   x += 1

print result
   

# Hm...this never terminates, obviously. I just let it run for a while until it had found
# two, added them and found the result ;-)
