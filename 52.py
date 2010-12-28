
def digits(i):
   return [int(c) for c in str(i)]

def examine(i):
   ds = digits(i*2)

   for mul in [i*x for x in range(3, 7)]:
      for x in digits(mul):
         if not x in ds:
            return False
   return True
   
i = 1
while True:
   if examine(i):
      print "Found:", i
      break
      
   i += 1
            

