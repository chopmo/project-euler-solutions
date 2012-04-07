class Solver
  def self.solve(input)
    new(input).result
  end

  def initialize(input)
    @cells = input.lines.map { |line| line.split(/,/).map(&:strip).map(&:to_i) }
    @best_trail = nil
  end

  attr_reader :cells

  def result
    find_best_trail(0, 0)
    trail_sum(@best_trail)
  end

  def find_best_trail(r, c, trail = [])
    trail << val(r, c)
    if r == last_row
      if c == last_col
        update_best_trail(trail)
      else
        find_best_trail(r, c + 1, trail.dup)
      end
    else
      # not the last row
      if c == last_col
        find_best_trail(r + 1, c, trail.dup)
      else
        find_best_trail(r, c + 1, trail.dup)
        find_best_trail(r + 1, c, trail.dup)
      end
    end
  end

  def update_best_trail(trail)
    if @best_trail.nil? || trail_sum(trail) < trail_sum(@best_trail)
      @best_trail = trail
    end
  end

  def trail_sum(trail)
    trail.inject(&:+) || 0
  end

  def val(row, col)
    cells[row][col]
  end
  
  def last_row
    cells.size - 1
  end

  def last_col
    cells[0].size - 1
  end
end
