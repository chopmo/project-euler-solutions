require 'mathn'

class Integer
  def prime?
    pd = self.prime_division
    pd.size == 1 && pd[0][1] == 1
  end
end
