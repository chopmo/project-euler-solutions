class Solver
  Node = Struct.new(:row, :col, :val, :dist)

  def self.solve(input)
    new(input).result
  end

  def initialize(input)
    @cells = []
    input.lines.each_with_index do |line, row_idx|
      row = []
      line.split(/,/).each_with_index do |num_string, col_idx|
        number = num_string.strip.to_i
        row << Node.new(row_idx, col_idx, number, 1_000_000)
      end
      @cells << row
    end
    
    @current = @cells[0][0]
    @current.dist = @current.val

    @unvisited = @cells.flatten
    @unvisited.delete(@current)
  end

  attr_reader :cells, :unvisited

  def neighbours(n)
    res = []
    res << cells[n.row + 1][n.col] if n.row < last_row
    res << cells[n.row][n.col + 1] if n.col < last_col
    res
  end
  
  def result
    visit_nodes
    last_node = cells.last.last
    last_node.dist
  end

  def visit_nodes
    while @current
      neighbours(@current).each do |n|
        n.dist = [n.dist, @current.dist + n.val].min
      end
      unvisited.delete(@current)
      @current = unvisited.first
    end
  end
  
  def last_row
    cells.size - 1
  end

  def last_col
    cells[0].size - 1
  end
end
