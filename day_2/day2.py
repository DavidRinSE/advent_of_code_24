from typing import List, Tuple

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
def check_report(r: List[int]) -> bool:
    diffs = [r[i + 1] - r[i] for i in range(len(r) - 1)]    # list differences between consecutive pairs
    if (all(x < 0 and x in range(-3, 0) for x in diffs) or  # all differences are negative and between -3 and -1
      all(x > 0 and x in range(1, 4) for x in diffs)):    # all differences are positive and between 1 and 3
        return True
    else:
        return False

def count_safe_reports(data: List[List[int]]) -> Tuple[int, int]:
    count = 0
    dampened_count = 0
    for row in data:
        if check_report(row):
            count += 1
            dampened_count += 1
        else:
            for i in range(len(row)):
                temp_row = row.copy()
                temp_row.pop(i)
                if check_report(temp_row):
                    dampened_count += 1  # report is safe by removing a single level
                    break

    return count, dampened_count

def main():
    data = read_file("input.txt")
    safe_reports_count, safe_reports_dampened_count = count_safe_reports(data)

    print("Number of safe reports:", safe_reports_count)
    print("Number of safe reports with dampener:", safe_reports_dampened_count)

if __name__ == "__main__":
    main()
