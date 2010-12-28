
def digits(x)
  if x < 10
    [x]
  else
    digits(x / 10) + [x % 10]
  end
end

def 
