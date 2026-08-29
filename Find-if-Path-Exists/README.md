# Find if Path Exists in Graph

## A. Title of the Problem

Find if Path Exists in Graph

## B. Problem Statement

You are given a graph consisting of a number of nodes and edges.

The graph is represented using a list of edges, where each edge connects
two nodes. Given a source node and a destination node, the objective is
to determine whether there exists a valid path from the source node to
the destination node.

If a path exists between the source and destination, the solution should
return `true`. Otherwise, it should return `false`.

## C. LeetCode Link

[Find if Path Exists in Graph - LeetCode](https://leetcode.com/problems/find-if-path-exists-in-graph/?utm_source=chatgpt.com)

## D. GitHub Repository

This repository contains the Python implementation of the solution.

The complete source code is available in:

`solution.py`

## E. Solution Steps / Algorithm

The problem can be solved using graph traversal.

### Steps

1. Create an adjacency list to represent the graph.
2. Add both directions of every edge because the graph is undirected.
3. Start the traversal from the given source node.
4. Maintain a set or array to keep track of visited nodes.
5. Visit all nodes connected to the current node.
6. If the destination node is reached, return `true`.
7. Continue the traversal until all reachable nodes have been explored.
8. If the destination cannot be reached, return `false`.

### Graph Traversal

The solution can use either:

- Breadth-First Search (BFS), or
- Depth-First Search (DFS)

The implementation in `solution.py` contains the actual approach used
for solving the problem.

### Complexity

- Time Complexity: O(V + E)
- Space Complexity: O(V + E)

Where:

- `V` = number of vertices/nodes
- `E` = number of edges

## F. Code Developed

The solution was implemented in Python.

The complete source code is available in:

`solution.py`

## G. Test Case / Output

The solution was tested using the test cases provided by LeetCode.

The output confirms whether a valid path exists between the given source
and destination nodes.

## H. Observation

The problem was solved using graph traversal. An adjacency list is used
to represent the connections between nodes, and visited nodes are tracked
to avoid processing the same node repeatedly.

The traversal successfully determines whether the destination node is
reachable from the source node.
