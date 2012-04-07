# Very slow, takes minutes

class Integer
  def fact
    (2..self).inject(1) { |f, n| f * n }
  end
end

def fact_sum(i)
  res = 0
  while i > 0
    res += (i % 10).fact
    i /= 10
  end
  res
end

def num_non_repeating_terms(i)
  terms = [i]
  while s = fact_sum(i) and !terms.include?(s)
    terms << s
    i = s
  end
  terms.size
end

count = 0
1.upto(1_000_000) do |i|
  if num_non_repeating_terms(i) == 60
    count += 1
  end
end

puts count
