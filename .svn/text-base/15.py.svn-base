import re

def say(number):
   words = {
      1: "one",
      2: "two",
      3: "three",
      4: "four",
      5: "five",
      6: "six",
      7: "seven",
      8: "eight",
      9: "nine",
      10: "ten",
      11: "eleven",
      12: "twelve",
      13: "thirteen",
      14: "fourteen",
      15: "fifteen",
      16: "sixteen",
      17: "seventeen",
      18: "eighteen",
      19: "nineteen",
      20: "twenty",
      30: "thirty",
      40: "forty",
      50: "fifty",
      60: "sixty",
      70: "seventy",
      80: "eighty",
      90: "ninety",
      1000: "one thousand"
   }
   if words.has_key(number):
      result = words[number]
   elif number >= 100:
      hundreds = number / 100
      result = say(hundreds) + " " + "hundred"
      remainder = number % 100
      if remainder > 0:
         result += " and " + say(remainder)
   else:
      # eg. forty-two
      result = words[10 * (number / 10)] + "-" + words[number % 10]

   return result

def remove_non_letters(s):
   return re.sub("[^a-z]", "", s)

count = 0
for x in range(1,1001):
   count += len(remove_non_letters(say(x)))

print "Result:", count
