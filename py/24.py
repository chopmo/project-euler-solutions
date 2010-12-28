# XXX: NOT complete!


def permutation(k, s):
   n = len(s)
   factorial = 1
   for j in xrange(2, n-1):      # compute (n- 1)!
      factorial = factorial * j
      for j in xrange(1, n-1):
         tempj = (k / factorial) % (n + 1 - j)
         temps = s[j + tempj]
         for i in xrange(j + tempj, j + 1):
            s[i] = s[i- 1] # shift the chain right
            
         s[j] = temps
         factorial = factorial / (n - j)
         
   return s

print permutation(10, [1,2,3,4])
