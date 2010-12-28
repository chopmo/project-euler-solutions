#!/usr/bin/python

# Find the difference between the sum of the squares of the first one hundred natural
# numbers and the square of the sum.

first_100_natural = range(1, 101)

sum_of_sqr = sum([x * x for x in first_100_natural])
sqr_of_sum = sum(first_100_natural) * sum(first_100_natural)

print "Result: " + str(sqr_of_sum - sum_of_sqr)
