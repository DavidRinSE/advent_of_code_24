from typing import List, Tuple

# Read the columns from day one input and return them as two lists
def read_columns(file_path: str) -> Tuple[List[str], List[str]]:
    column1: List[str] = []
    column2: List[str] = []
    
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by whitespace
            parts = line.split()
            if len(parts) == 2:  # Ensure there are exactly two columns
                column1.append(parts[0])
                column2.append(parts[1])
    
    return column1, column2