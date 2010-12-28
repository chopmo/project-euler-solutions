import re
import string

# Load and prepare data
names_str = open("22_names.txt").read()
names = []
for quoted_name in names_str.split(","):
   names.append(re.sub("[^A-Z]", "", quoted_name))

names.sort()

def name_score(name):
   return sum(string.uppercase.find(letter) + 1 for letter in name)

def alpha_score(name):
   result = 1
   for k in names:
      if k == name:
         return result
      result += 1

def score(name):
   return name_score(name) * alpha_score(name)
      
print sum(score(name) for name in names)




# Pasting "Begoner"s version here for inspiration:
# # First load the file and sort it.
 
# x = eval( '[' + open( '.../names.txt' ).readlines()[ 0 ] + ']' )
# x.sort()
 
# # Then calculate what is needed.
 
# reduce( lambda x, y: x + y, [ reduce( lambda x, y: x + y, [ ( j + 1 ) * ( ord( i ) - 64 ) for i in x[ j ] ] ) for j in xrange( len( x ) ) ] )
