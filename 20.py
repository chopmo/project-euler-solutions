
number = 1
for x in range(1, 101):
   number *= x

print number

print sum(int(i) for i in str(number))
