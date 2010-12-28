

def spiral_sum(size):
   result = 1
   jump_dist = 2
   current_number = 1
   for layer in range(0, size/2):
      # Add 4 diagonals
      for i in range(4):
         current_number += jump_dist
         result += current_number

      jump_dist += 2

   return result

print spiral_sum(1001)
