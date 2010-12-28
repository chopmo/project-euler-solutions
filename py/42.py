from utils import *

def letter_value(c):
   return ord(c) - 64

def word_value(s):
   return sum([letter_value(c) for c in s])

words = eval ("[" + file("42_words.txt").read() + "]")

tg = TriangleNumberGenerator()
print len(filter(lambda n: tg.is_triangle_number(word_value(n)), words))
