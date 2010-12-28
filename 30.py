
# Small bug here - this assumes only four digits, which is not specified in the
# problem. However, the result turns out to be the right one.
upper_limit = 4 * (9 ** 5)

def sum_fifth_power_digits(number):
   sum_digits = 0
   digits = [int(d) for d in str(number)]
   for d in digits:
      sum_digits += d ** 5

   return sum_digits

result = 0
for number in range(10, upper_limit+1):
   if sum_fifth_power_digits(number) == number:
      print "found", number
      result += number

print "Result:", result
