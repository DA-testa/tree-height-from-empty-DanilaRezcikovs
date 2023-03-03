# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Create a list to store the depth of each node
    depth = [0] * n

    # Find the root node
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = i
            break

    # Recursively traverse each subtree and update the depth of each node
    def traverse(node):
        if depth[node] != 0:
            return depth[node]

        if parents[node] == -1:
            depth[node] = 1
        else:
            depth[node] = 1 + traverse(parents[node])

        return depth[node]

    # Traverse the tree starting from the root
    traverse(root)

    # Return the maximum depth
    return max(depth)

# Read input
n = int(input())
parents = list(map(int, input().split()))

# Compute and print the height of the tree
print(compute_height(n, parents))
