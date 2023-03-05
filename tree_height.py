import os

class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.children = []

def compute_height(nodes):
    root = None
    for i, node in enumerate(nodes):
        if node.value == -1:
            root = i
        else:
            nodes[node.value].children.append(node)
    if root is not None:
        root_node = nodes[root]
        return get_height(root_node)
    else:
        return 0


def get_height(node):
    if not node.children:
        return 1
    heights = [get_height(child) for child in node.children]
    height = 1 + max(heights)
    return height


def main():
    input_type = input("Input data from keyboard (I) or file (F)? ").upper()
    while input_type not in ['I', 'F']:
        print("Invalid input. Please enter I or F.")
        input_type = input("Input data from keyboard (I) or file (F)? ").upper()

    if input_type == 'I':
        n_str = input("Enter the number of nodes: ")
        while not n_str.isdigit():
            print("Invalid input. Please enter a positive integer.")
            n_str = input("Enter the number of nodes: ")
        n = int(n_str)

        values_str = input("Enter the values for each node: ")
        while len(values_str.split()) != n:
            print(f"Invalid input. Please enter {n} values.")
            values_str = input("Enter the values for each node: ")
        values = list(map(int, values_str.split()))

    else:
        file_name = input("Enter the file name (without letter 'a'): ")
        while 'a' in file_name:
            print("Invalid file name. Please enter a file name without the letter 'a'.")
            file_name = input("Enter the file name (without letter 'a'): ")
        file_path = os.path.join('test', file_name)
        with open(file_path, 'r') as f:
            n = int(f.readline())
            values = list(map(int, f.readline().split()))

    nodes = [Node(i, values[i]) for i in range(n)]
    print(compute_height(nodes))


if __name__ == '__main__':
    main()
