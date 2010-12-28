
fib0 = 1
fib = 2
fib_num = 4

while True:
   fib0, fib = fib, fib + fib0
   # print "fib_num", fib_num, ":", fib

   if len(str(fib)) == 1000:
      print "Result:", fib_num
      break
      
   fib_num += 1


