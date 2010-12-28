
terms = set()

def is_pandigital(a, b, x):
   digits = set()
   [digits.add(c) for c in str(a)]
   [digits.add(c) for c in str(b)]
   [digits.add(c) for c in str(x)]
   return len(digits) == 9 and (not '0' in digits)

for a in range(2,101):
   for b in range(2,101):
      terms.add(a**b)

print "result:", len(terms)
      
