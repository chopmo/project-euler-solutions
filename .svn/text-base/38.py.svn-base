
def is_pandigital(s):
   digits = set()
   [digits.add(c) for c in str(s)]
   return len(digits) == 9 and (not '0' in digits)

max_pan = 0
for i in xrange(1, 33333):
   n = 1
   s = ""
   while True:
      s += str(n * i)
      n += 1
      if len(s) > 9:
         break
      
      if is_pandigital(s) and int(s) > max_pan:
         print "Found:", s
         max_pan = int(s)

      
