require 'utils'

require 'mathn'
require 'set'

class Problem50
  def initialize
    print "Caching primes..."
    @primes = []
    Prime.instance.each do |p|
      break if p > 1000000
      @primes << p
    end
    puts "done."
  end


  # I had a lot of trouble with this one. Initial strategy was to find
  # the max length for each prime, but it takes forever (obviously, I
  # guess). #solve2 take very little time to run.
  
  # def solve
  #   result = 0
  #   max_len = 0
  #   @primes.each do |k|
  #     longest_seq = find_longest_seq(k)
  #     if longest_seq > max_len
  #       max_len = longest_seq
  #       result = k
  #       puts "New max: #{max_len} at prime #{result}"
  #     end
  #   end
  #   result
  # end

  # def find_longest_seq(x)
  #   longest = 0
  #   for p1_idx in (0..@primes.size)
  #     for p2_idx in (p1_idx..@primes.size)
  #       s = sum_primes_between(p1_idx, p2_idx)
  #       if s > x
  #         break
  #       elsif s == x
  #         longest = [longest, p2_idx + 1 - p1_idx].max
  #       end
  #     end
  #     break if @primes[p1_idx] > x
  #   end
  #   longest
  # end

  def sum_primes_between(idx1, idx2)
    @primes.slice(idx1, idx2 - idx1 + 1).reduce(:+)
  end


  # Alterntive strategy: Sweep increasing lengths
  def solve2
    len = 21 # We know this is < 1000
    max_len = 21
    result = 0
    while true
      len += 1
      p = find_prime_seq(len)
      if p and p > result
        result = p
        puts "New max: #{len} at prime #{result}"
      end
    end
  end

  # Try finding a sequence of length "len" that sums up to a prime below 1 million
  # Hangs/works for a long time after finding the answer
  def find_prime_seq(len)
    for start_idx in (0..@primes.size-1)
      end_idx = start_idx + len - 1
      break if end_idx > @primes.size
      s = sum_primes_between(start_idx, end_idx)
      break if s > @primes[-1]
      return s if s.prime?
    end
    nil
  end
end


Problem50.new.solve2
