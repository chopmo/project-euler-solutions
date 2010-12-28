
def transform(n):
   if n % 2 == 0:
      return n / 2
   else:
      return 3 * n + 1

def int_seq_len(n):
   # result = [n]
   result_len = 1
   while n != 1:
      n = transform(n)
      # result.append(n)
      result_len += 1
      
   # return result
   return result_len

max_len = 0
for x in range(1, 1000000):
   l = int_seq_len(x)
   if l > max_len:
      print "found new max:", l, "at", x
      max_len = l

print "Result:", max_len
