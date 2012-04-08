# Very slow, takes minutes

$fact_cache = {}

class Integer
  def fact
    $fact_cache[self] ||= (2..self).inject(1) { |f, n| f * n }
  end

  def fact_sum
    i = self
    res = 0
    while i > 0
      res += (i % 10).fact
      i /= 10
    end
    res
  end
end

@chain_lengths = {}
def num_non_repeating_terms(i)
  x = i
  terms = [i]
  chain_length = 1
  while s = x.fact_sum and !terms.include?(s)
    if cached = @chain_lengths[s]
      # puts "found #{cached} for #{s}"
      chain_length += cached
      break
    end
    terms << s
    chain_length += 1
    x = s
  end
  # puts "calc #{chain_length} for #{i}"
  @chain_lengths[i] = chain_length
end

count = 0
1.upto(1_000_000) do |i|
  if num_non_repeating_terms(i) == 60
    count += 1
    # puts i
  end

  # $stdout.write(".") if i % 10_000 == 0
end
  

puts count
