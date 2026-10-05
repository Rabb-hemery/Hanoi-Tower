# Tower of Hanoi Solver

A Python implementation of the classic **Tower of Hanoi** mathematical puzzle using a recursive algorithm. This program tracks and outputs the state of all three rods after every individual move.

## 📋 Project Rules

The puzzle starts with n disks stacked in decreasing order of size on the first rod (smallest disk is represented by `1`). The objective is to move the entire stack to the last rod, obeying the following rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
3. No larger disk may be placed on top of a smaller disk.

The optimal number of steps required to solve a Tower of Hanoi puzzle is \(2^n - 1\).

## 🚀 Features

- **Recursive Logic:** Implements the optimal mathematical solution.
- **State Tracking:** Returns the complete breakdown of every move step-by-step.
- **Clean Formatting:** Matches strict automation test environments (outputting precise lists representation).

## 💻 Usage

```python
from hanoi_tower import hanoi_solver

# Generate the step-by-step solution for 3 disks
solution = hanoi_solver(3)
print(solution)
```

### Example Output (for 3 disks)

```text
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```
