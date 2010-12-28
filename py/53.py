from utils import *

def ncr(n, r):
   return fact(n) / (fact(r) * fact(n-r))

result = 0
for n in range(1, 101):
   for r in range(0, n+1):
      if ncr(n, r) > 1000000:
         result += 1

print result
