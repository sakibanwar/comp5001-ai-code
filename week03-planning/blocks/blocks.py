"""
Blocks World planner - COMP5001 Week 3 (Planning)

A state is a set of facts, e.g. On(C, A) or Clear(B).
Each action has preconditions and effects (STRIPS style).
We find a plan with the same search code as maze.py from Week 2.

Usage: python blocks.py problem0.txt [bfs|dfs]
"""

import sys


# ---------------------------------------------------------------
# Facts
# ---------------------------------------------------------------

def On(block, below):
    return ("On", block, below)


def Clear(block):
    return ("Clear", block)


def show_fact(fact):
    return f"{fact[0]}({', '.join(fact[1:])})"


# ---------------------------------------------------------------
# Actions
# ---------------------------------------------------------------

class Action():
    def __init__(self, name, preconditions, add, delete):
        self.name = name
        self.preconditions = preconditions
        self.add = add
        self.delete = delete

    def applicable(self, state):
        """An action can be taken if all its preconditions are true."""
        return self.preconditions <= state

    def result(self, state):
        """Remove the delete facts, then add the add facts."""
        return (state - self.delete) | self.add


def all_actions(blocks):
    """Every Move and MoveToTable action for these blocks."""
    actions = []
    for b in blocks:
        for x in blocks + ["Table"]:
            if x == b:
                continue

            # Move(b, x, y): move block b from x onto block y
            for y in blocks:
                if y == b or y == x:
                    continue
                add = {On(b, y)}
                if x != "Table":
                    add.add(Clear(x))  # the table always has room, so we never track Clear(Table)
                actions.append(Action(
                    name=f"Move({b}, {x}, {y})",
                    preconditions={On(b, x), Clear(b), Clear(y)},
                    add=add,
                    delete={On(b, x), Clear(y)}
                ))

            # MoveToTable(b, x): move block b from block x onto the table
            if x != "Table":
                actions.append(Action(
                    name=f"MoveToTable({b}, {x})",
                    preconditions={On(b, x), Clear(b)},
                    add={On(b, "Table"), Clear(x)},
                    delete={On(b, x)}
                ))
    return actions


# ---------------------------------------------------------------
# Search (same idea as maze.py)
# ---------------------------------------------------------------

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class Problem():

    def __init__(self, filename):
        self.blocks, self.initial, self.goal = read_problem(filename)
        self.actions = all_actions(self.blocks)
        self.solution = None

    def solve(self, method="bfs"):
        """Finds a plan (a list of actions) that reaches the goal."""

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier to just the initial state
        start = Node(state=frozenset(self.initial), parent=None, action=None)
        frontier = StackFrontier() if method == "dfs" else QueueFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no plan
            if frontier.empty():
                raise Exception("no plan")

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # Goal test: are all the goal facts true in this state?
            if self.goal <= node.state:
                plan = []
                states = []
                while node.parent is not None:
                    plan.append(node.action)
                    states.append(node.state)
                    node = node.parent
                plan.reverse()
                states.reverse()
                self.solution = (plan, states)
                return

            # Mark node as explored
            explored.add(node.state)

            # Add the result of every applicable action to the frontier
            for action in self.actions:
                if action.applicable(node.state):
                    state = frozenset(action.result(node.state))
                    if not frontier.contains_state(state) and state not in explored:
                        child = Node(state=state, parent=node, action=action)
                        frontier.add(child)


# ---------------------------------------------------------------
# Reading problems and printing states
# ---------------------------------------------------------------

def stacks_to_facts(stacks):
    """Turn stacks (bottom to top) into On and Clear facts."""
    facts = set()
    for stack in stacks:
        facts.add(On(stack[0], "Table"))
        for below, block in zip(stack, stack[1:]):
            facts.add(On(block, below))
        facts.add(Clear(stack[-1]))
    return facts


def read_problem(filename):
    """
    File format: one stack per line, listed from bottom to top.
    Lines under 'initial:' describe the start, lines under 'goal:' the goal.
    """
    sections = {"initial": [], "goal": []}
    current = None
    with open(filename) as f:
        for line in f:
            line = line.split("#")[0].strip()
            if not line:
                continue
            if line.rstrip(":") in sections:
                current = line.rstrip(":")
            elif current is None:
                raise Exception("file must start with 'initial:'")
            else:
                sections[current].append(line.split())

    blocks = sorted(b for stack in sections["initial"] for b in stack)
    goal_blocks = sorted(b for stack in sections["goal"] for b in stack)
    if blocks != goal_blocks:
        raise Exception("initial and goal must use the same blocks")

    initial = stacks_to_facts(sections["initial"])

    # The goal only says which block is on which block
    goal = {fact for fact in stacks_to_facts(sections["goal"])
            if fact[0] == "On" and fact[2] != "Table"}
    return blocks, initial, goal


def draw(state):
    """Print the stacks in a state as a small picture."""
    on_table = sorted(fact[1] for fact in state if fact[0] == "On" and fact[2] == "Table")
    stacks = []
    for bottom in on_table:
        stack = [bottom]
        while True:
            above = [fact[1] for fact in state if fact[0] == "On" and fact[2] == stack[-1]]
            if not above:
                break
            stack.append(above[0])
        stacks.append(stack)
    height = max(len(stack) for stack in stacks)
    for level in reversed(range(height)):
        print("    " + "  ".join(f"[{s[level]}]" if level < len(s) else "   " for s in stacks))
    print("    " + "=" * (5 * len(stacks) - 2))


def main():
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python blocks.py problem.txt [bfs|dfs]")
    method = sys.argv[2] if len(sys.argv) == 3 else "bfs"
    if method not in ["bfs", "dfs"]:
        sys.exit("Search method must be bfs or dfs")

    p = Problem(sys.argv[1])

    print("Initial state:")
    draw(p.initial)
    print("  Facts: " + ", ".join(sorted(show_fact(f) for f in p.initial)))
    print()
    print("Goal: " + " ∧ ".join(sorted(show_fact(f) for f in p.goal)))
    print()

    print(f"Solving with {method.upper()}...")
    p.solve(method)
    plan, states = p.solution
    print(f"States explored: {p.num_explored}")
    print(f"Plan length: {len(plan)}")
    print()

    for i, (action, state) in enumerate(zip(plan, states), start=1):
        print(f"Step {i}: {action.name}")
        draw(state)
        print()


if __name__ == "__main__":
    main()
