#!/usr/bin/python

f0, f = 1, 2
sum = 2

while True:
   f0, f = f, f0 + f # f=3
   f0, f = f, f0 + f # f=5
   f0, f = f, f0 + f # f=8

   if f >= 4000000:
      break
   
   sum += f

print sum

