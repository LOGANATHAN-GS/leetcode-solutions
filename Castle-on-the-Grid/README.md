# Castle on the Grid

## A. Title of the Problem

Castle on the Grid

## B. Problem Statement

Given a square grid containing open cells represented by `.` and blocked
cells represented by `X`, the player has to move from a given starting
position to a given goal position.

The player can move horizontally or vertically through open cells.
During one move, the player can continue moving in one direction until
reaching the edge of the grid or a blocked cell.

The objective is to determine the minimum number of moves required to
reach the goal position from the starting position.

## C. HackerRank Link

[Castle on the Grid - HackerRank](https://www.hackerrank.com/challenges/castle-on-the-grid/problem?utm_source=chatgpt.com)

## D. GitHub Repository

This repository contains the Python implementation of the Castle on the
Grid problem.

The complete source code is available in:

`main.py`

## E. Solution Steps / Algorithm

The problem is solved using Breadth-First Search (BFS).

### Steps

1. Start from the given starting position.
2. Create a queue to store the positions that need to be explored.
3. Create a visited array to store the minimum number of moves required
   to reach each cell.
4. Mark the starting position as visited with distance `0`.
5. From the current position, explore all four directions:
   - Down
   - Up
   - Right
   - Left
6. Continue moving in each direction until reaching the boundary of the
   grid or a blocked cell `X`.
7. If an unvisited valid cell is found, mark it as visited.
8. Store the number of moves required to reach that cell.
9. Add the cell to the BFS queue.
10. Continue the process until the goal position is reached.
11. Return the minimum number of moves.

### Complexity

- Time Complexity: O(n²)
- Space Complexity: O(n²)

## F. Code Developed

The solution was implemented in Python using Breadth-First Search (BFS).

The complete code is available in:

`main.py`

## G. HackerRank Test Case

The solution was tested on HackerRank.

A screenshot showing the successful HackerRank submission/test cases
is included in the assignment report.

## H. Observation

The problem was successfully solved using Breadth-First Search (BFS).
BFS explores the possible positions level by level, ensuring that the
minimum number of moves required to reach the goal is obtained.

The solution also avoids blocked cells and stops movement when the edge
of the grid or a blocked cell is reached.
