
@count = 0
@coins = [200, 100, 50, 20, 10, 5, 2, 1, 0]

def iterate_coin(coin, sum)
  (0...201).step(coin) do |x|
    break if sum + x > 200
    yield sum + x
  end
end

def coin(idx, sum)
  coin_value = @coins[idx]
  if coin_value == 0
    if sum == 200
      @count += 1
    end
  else
    iterate_coin(coin_value, sum) do |sum|
      coin(idx + 1, sum)
    end
  end
end

coin(0, 0)

# iterate_coin(200, 0) do |sum|
#   iterate_coin(100, sum) do |sum|
#     iterate_coin(50, sum) do |sum|
#       iterate_coin(20, sum) do |sum|
#         iterate_coin(10, sum) do |sum|
#           iterate_coin(5, sum) do |sum|
#             iterate_coin(2, sum) do |sum|
#               iterate_coin(1, sum) do |sum|
#                 if sum == 200
#                   count += 1
#                 end
#               end
#             end
#           end
#         end
#       end
#     end
#   end
# end

puts @count

