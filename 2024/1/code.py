# Advent of Code ~ (2024) - Day 1 Solution
# -----------------
# Author: WildZarek
# Date: December 2024

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

# Split the lines into pairs of numbers
pairs = [tuple(map(int, line.split())) for line in input]
# Sort by the first and second columns
sorted_l_column = [x[0] for x in sorted(pairs, key=lambda x: x[0])]
sorted_r_column = [x[1] for x in sorted(pairs, key=lambda x: x[1])]
# Calculate each difference between two numbers and store them in a list
results = [
    abs(l_number - r_number)
    for l_number, r_number in zip(sorted_l_column, sorted_r_column)
]

print(f"Part One: {str(sum(results))}")

# Count occurrences of each number in the left column in the right column
count_dict = {num: sorted_r_column.count(num) for num in sorted_l_column}
# Multiply each number by its count and store the results in a list
results = [num * count for num, count in count_dict.items()]

print(f"Part Two: {str(sum(results))}")