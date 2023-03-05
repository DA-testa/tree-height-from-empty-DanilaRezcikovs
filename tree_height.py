# python3

import sys
import threading
import numpy


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

n = int(input().strip())
parent_indices = list(map(int, input().strip().split()))

nodes = [Node(i) for i in range(n)]

for i in range(n):
    parent_index = parent_indices[i]
    if parent_index == -1:
        root = nodes[i]
    else:
        parent_node = nodes[parent_index]
        parent_node.children.append(nodes[i])
        nodes[i].parent = parent_node

def max_depth(node):
    if not node.children:
        return 1
    else:
        return 1 + max(max_depth(child) for child in node.children)

height = max_depth(root)
print(height)
