# python3

import sys
import threading
import numpy
import re


class Node:
    def __init__(self, index):
        self.index = index
        self.children = []

def compute_height(nodes):
    root = None
    for i, parent_index in enumerate(nodes):
        if parent_index == -1:
            root = i
        else:
            nodes[parent_index].children.append(nodes[i])
    return get_height(root)

def get_height(node):
    if not node.children:
        return 1
    return 1 + max([get_height(child) for child in node.children])

if __name__ == '__main__':
    import os

    input_type = input("Input data from keyboard (I) or file (F)? ").upper()
    while input_type not in ['I', 'F']:
        print("Invalid input. Please enter I or F.")
        input_type = input("Input data from keyboard (I) or file (F)? ").upper()

    if input_type == 'I':
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the list of parents for each node (-1 for root): ").split()))
    else:
        file_name = input("Enter the file name (without letter 'a'): ")
        while 'a' in file_name:
            print("Invalid file name. Please enter a file name without the letter 'a'.")
            file_name = input("Enter the file name (without letter 'a'): ")
        file_path = os.path.join('folder', file_name)
        with open(file_path, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))

    nodes = [Node(i) for i in range(n)]
    print(compute_height(nodes))
