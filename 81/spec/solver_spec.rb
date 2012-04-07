require 'solver'

describe Solver do
  it 'solves the sample problem' do
    input = open(File.join(File.dirname(__FILE__), "../data/sample.txt")).read
    Solver.solve(input).should == 2427
  end
end
