# From http://www.daniweb.com/code/snippet285.html
def Denary2Binary(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr



def is_palindromic(s):
   s2 = s
   while len(s2) > 1:
      if not s2[0] == s2[-1]:
         return False
      
      s2 = s2[1:-1]
   return True

result = 0
for i in range(1000000):
   if is_palindromic(str(i)) and is_palindromic(Denary2Binary(i)):
      result += i


print "result", result
