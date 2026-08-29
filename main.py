#!/bin/python3

import math
import os
import random
import re
import sys


def minimumMoves(grid, startX, startY, goalX, goalY):

    n = len(grid)

    # Queue for BFS
    queue = [(startX, startY)]

    # visited[x][y] stores minimum number of moves
    visited = [[-1] * n for _ in range(n)]

    # Starting position
    visited[startX][startY] = 0

    # Down, Up, Right, Left
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    front = 0

    while front < len(queue):

        x, y = queue[front]
        front += 1

        # Reached goal
        if x == goalX and y == goalY:
            return visited[x][y]

        # Try all 4 directions
        for dx, dy in directions:

            newX = x + dx
            newY = y + dy

            # Keep moving until wall or edge
            while (
                0 <= newX < n and
                0 <= newY < n and
                grid[newX][newY] != 'X'
            ):

                # Visit only if not visited before
                if visited[newX][newY] == -1:

                    visited[newX][newY] = visited[x][y] + 1

                    queue.append((newX, newY))

                # Continue in same direction
                newX += dx
                newY += dy

    return -1


# -------------------------------
# VS CODE INPUT
# -------------------------------

if __name__ == '__main__':

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(input().strip())

    startX, startY, goalX, goalY = map(
        int, input().split()
    )

    result = minimumMoves(
        grid,
        startX,
        startY,
        goalX,
        goalY
    )

    print(result)