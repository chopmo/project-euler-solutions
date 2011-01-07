require 'mathn'

def solve(num_factors)
  target_hit_count = 0
  x = 10
  while true
    #factors = factorize(x)
    if x.prime_division.size == num_factors
      target_hit_count += 1
    else
      target_hit_count = 0
    end
    if target_hit_count == num_factors
      first_x = x - num_factors + 1
      puts "First x: #{first_x}"
      break
    end
    x += 1
    puts "#{x} #{target_hit_count}"
  end
end

solve(4)
