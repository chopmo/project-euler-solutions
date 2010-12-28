import time

class Timer:
   def __enter__(self):
      self.t0 = time.time()

   def __exit__(self, type, value, tb):
      print "Time: " + str(time.time() - self.t0)
