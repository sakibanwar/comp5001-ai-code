COMP5001 Week 3 Practical: Planning
===================================

Files
  blocks.py      A planner for Blocks World. It uses the same search code as maze.py.
  problem0.txt   The example from the slides (3 blocks)
  problem1.txt   4 blocks
  problem2.txt   Turn a tower of 5 blocks upside down
  domain.pddl    The Blocks World actions written in PDDL
  problem0.pddl  Problem 0 written in PDDL

Problem files list one stack per line, from bottom to top.

Task 1  Run the planner
  python blocks.py problem0.txt
  Check the plan matches the one from the slides.

Task 2  BFS or DFS?
  python blocks.py problem2.txt bfs
  python blocks.py problem2.txt dfs
  Compare the plan lengths and the number of states explored. Why is the DFS plan so long?

Task 3  Write your own problem
  Make problem3.txt with 4 or 5 blocks. Predict the plan length before you run it.

Task 4  Read the actions
  Find all_actions() in blocks.py. Match each line to the preconditions and effects on the slides.
  What would go wrong if Move forgot the precondition Clear(y)? Try it.

Task 5  PDDL
  Go to https://editor.planning.domains
  Open domain.pddl and problem0.pddl (File > Load), then use Solver.
  Is the plan the same as the one from blocks.py?

Stretch
  Add A* search to blocks.py with the heuristic
  h(n) = number of goal facts that are not yet true.
  Does it explore fewer states than BFS on problem2.txt?
