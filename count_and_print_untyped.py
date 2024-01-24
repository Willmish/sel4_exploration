#!/opt/homebrew/Caskroom/miniconda/base/bin/python3

# This scripts counts up all untypeds and actual sizes created during memory reuse and free mem initial allocation
# and the dump from seL4_BootInfo. It then prints the counts side by side for comparison.

text = """
   """

import re

def count_bit_sizes_and_exponents(text):
    # Regular expression patterns
    actual_size_pattern = r"Actual size: (\d+)"
    untyped_size_pattern = r"\s2\^(\d+)\s+untyped"

    # Find all occurrences and convert to integers
    actual_sizes = [int(match) for match in re.findall(actual_size_pattern, text)]
    untyped_exponents = [int(match) for match in re.findall(untyped_size_pattern, text)]

    # Count occurrences
    actual_size_count = {size: actual_sizes.count(size) for size in set(actual_sizes)}
    untyped_exponent_count = {exp: untyped_exponents.count(exp) for exp in set(untyped_exponents)}

    return actual_size_count, untyped_exponent_count

def print_side_by_side(column1, column2):
    max_key = max(max(column1.keys(), default=0), max(column2.keys(), default=0))
    print(f"{'Actual Size Count':<20} | {'Untyped Exponent Count':<20}")
    print("-" * 43)

    for i in range(max_key + 1):
        col1_value = column1.get(i, '')
        col2_value = column2.get(i, '')
        print(f"{f'Size {i}: {col1_value}':<20} | {f'Exponent {i}: {col2_value}':<20}")


# Example usage
#text = """..."""  # replace with the input text
#text = open("./old_output").read()
text = open("./fixed_output").read()
actual_size_count, untyped_exponent_count = count_bit_sizes_and_exponents(text)
print_side_by_side(actual_size_count, untyped_exponent_count)
