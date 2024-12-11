from typing import Callable, List, Tuple

def read_file(file_path: str) -> List[List[int]]:
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into strings, then convert each to an integer
            row = [int(x) for x in line.split()]
            data.append(row)
    return data

# The data consists of many reports, one report per line. 
# Each report is a list of numbers called levels that are separated by spaces.
# A report is considered safe if
# 1. The levels are either all increasing or all decreasing.
# 2. Any two adjacent levels differ by at least one and at most three.
def check_report(row: List[int], is_increasing_check: bool) -> bool:
    for i in range(1, len(row)):
        if (row[i] > row[i-1]) != is_increasing_check: # >= cannot be used to check for repeating levels with this approach
            return False # Actual condition does not match test conditon
    
    # Successful order check
    # Ensure any two adjacent levels do not repeat and differ by at most three
    for i in range(1, len(row)):
        if row[i] == row[i - 1] or abs(row[i] - row[i - 1]) > 3:
            return False
    return True

# The Problem Dampener allows tollerance for one bad value in a safe report
# With the Problem Dampener the same rules apply for a safe report with one exception
def check_report_dampened(row: List[int], is_increasing_check: bool) -> bool:
    dampened = False
    is_ordered_row = row.copy()

    i = 1
    while i < len(is_ordered_row):
        if (is_ordered_row[i] > is_ordered_row[i - 1]) != is_increasing_check: # >= cannot be used to check for repeating levels with this approach
            # Order doesn't match, try to dampen the row
            if not dampened:
                if i == len(is_ordered_row) - 1:
                    is_ordered_row.pop(i)
                else:
                    is_ordered_row.pop(i - 1)
                dampened = True
            else:
                return False  # Already dampened, not safe
        else:
            i += 1  # Move to the next element
    
    # Successful order check
    
    # Ensure any two adjacent levels do not repeat using dampener
    i = 1
    while i < len(is_ordered_row):
        if is_ordered_row[i] == is_ordered_row[i-1]:
            if not dampened:
                if i == len(is_ordered_row) - 1:
                    is_ordered_row.pop(i)
                else:
                    is_ordered_row.pop(i - 1)
                dampened = True
            else:
                return False
        else:
            i += 1
    
    # Ensure any two adjacent levels do not differ by more than 3 using dampener
    i = 1
    while i < len(is_ordered_row):
        if abs(is_ordered_row[i] - is_ordered_row[i - 1]) > 3:
            if not dampened:
                if i == len(is_ordered_row) - 1:
                    is_ordered_row.pop(i)
                else:
                    is_ordered_row.pop(i - 1)
                dampened = True
            else:
                return False
        else:
            i += 1
    return True

def is_safe(row: List[int], check_function: Callable[[List[int]], bool]) -> bool:
    # First, check if the row is increasing
    if not check_function(row, True):
        # If increasing fails, check if it's decreasing
        if not check_function(row, False):
            return False  # Neither increasing nor decreasing is possible
    return True  # Checks pass, the row is safe

def count_safe_reports(data: List[List[int]]) -> Tuple[int, int]:
    count = 0
    dampened_count = 0
    for row in data:
        if is_safe(row, check_report):
            count += 1
        if is_safe(row, check_report_dampened):
            dampened_count += 1

    return count, dampened_count

def main():
    data = read_file("input.txt")
    safe_reports_count, safe_reports_dampened_count = count_safe_reports(data)

    print("Number of safe reports:", safe_reports_count)
    print("Number of safe reports with dampener:", safe_reports_dampened_count)

if __name__ == "__main__":
    main()

# Successful edge cases
# 48 46 47 49 51 54 56
# 1 1 2 3 4 5
# 1 2 3 4 5 5
# 5 1 2 3 4 5
# 1 4 3 2 1
# 1 6 7 8 9
# 1 2 3 4 3
# 9 8 7 6 7
# 7 10 8 10 11
# 29 28 27 25 26 25 22 20