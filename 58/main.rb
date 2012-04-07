require 'prime'


i = 1
side_length = 1
@diags = []
@primes = []

def count_primes
  @primes.size
end

def prime_ratio
  return 1 if @diags.empty?
  count_primes.to_f / @diags.size
end

while prime_ratio > 0.10
  side_length += 2
  4.times do
    i += (side_length - 1)
    @diags << i
    @primes << i if i.prime?
  end
end
puts "#{count_primes} primes (ratio #{prime_ratio}} for side length #{side_length}" 

