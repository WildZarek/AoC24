# Advent of Code ~ (2024) - Day 2 Solution
# -----------------
# Author: WildZarek
# Date: December 2024

with open((__file__.rstrip("code.py")) + "input.txt", 'r') as input_file:
    input = input_file.readlines()

def is_increasing_or_decreasing(numbers) -> bool:
    increasing = all(x < y for x, y in zip(numbers, numbers[1:]))
    decreasing = all(x > y for x, y in zip(numbers, numbers[1:]))
    return increasing or decreasing

def check_differences(line) -> bool:
    numbers = list(map(int, line.split()))
    for i in range(len(numbers) - 1):
        if not (1 <= abs(numbers[i] - numbers[i + 1]) <= 3):
            return False
    return True

def can_be_safe_by_removing_one(numbers) -> bool:
    for i in range(len(numbers)):
        new_numbers = numbers[:i] + numbers[i+1:]
        new_line = ' '.join(map(str, new_numbers))
        if is_increasing_or_decreasing(new_numbers) and check_differences(new_line):
            return True
    return False

part_one_safe_count = 0
part_two_safe_count = 0
for line in input:
    numbers = list(map(int, line.split()))
    if is_increasing_or_decreasing(numbers) and check_differences(line):
        part_one_safe_count += 1
    else:
        if can_be_safe_by_removing_one(numbers):
            part_two_safe_count += 1

print(f"Part One: {part_one_safe_count}")

print(f"Part Two: {part_one_safe_count + part_two_safe_count}")