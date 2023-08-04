# Imports
import sys
import time

# Variables
input_file = "input.txt"
output_file = "output.txt"
print_to_console = True
# dirs = 0
# files = []
bil = 1000000000  # 1 billion to simplify later calculations


# Functions
def generate_tree(file_paths):
    tree = {}  # A dictionary to store the tree structure

    for path in file_paths:
        components = path.split('\\')  # Split the path into components
        current_dict = tree

        for component in components:
            if component not in current_dict:
                current_dict[component] = {}  # Create a dictionary for the component
            current_dict = current_dict[component]

    return tree


def print_tree(tree, indent=0, output=sys.stdout):  # Add an output parameter
    for key, value in tree.items():
        print('\t' * indent + key, file=output)  # Print to the provided output
        if value:
            print_tree(value, indent + 1, output)


script_start_time = time.perf_counter_ns()

with open(input_file, "r") as file_list:
    files = [line.strip() for line in file_list.readlines()]

tree = generate_tree(files)
print_tree(tree)

with open(output_file, "w") as output_tsv:
    print_tree(tree, output=output_tsv)

script_end_time = time.perf_counter_ns()
script_time = (script_end_time - script_start_time) / bil
print(f"Read {len(files)} lines")
print(f"Script took {round(script_time, 2)} s")
