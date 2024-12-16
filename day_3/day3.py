import re

def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

# Corrupted data includes multiply instructions mul(x,x)
# Find all multiply instructions, multiply, then print a sum of them all
def partOne():
    input = read_file("input.txt")
    sum = 0
    matches = re.findall(r"mul\(([0-9]*),([0-9]*)\)", input)
    matches = [(int(a), int(b)) for a, b in matches]
    for match in matches:
        sum += match[0] * match[1]
    print(sum)

# Corrupted data also includes do() and don't() instructions
# don't() disables mul operations
# do() enables mul operations
# mul operations start enables
def partTwo():
    input = read_file("input.txt")
    sum = 0
    enabled = True
    matches = re.findall(r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)", input)
    for match in matches:
        if enabled and len(match[2]):
            sum += int(match[2]) * int(match[3])
        elif len(match[0]):
            enabled = True
        elif len(match[1]):
            enabled = False
    print(sum)

def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()