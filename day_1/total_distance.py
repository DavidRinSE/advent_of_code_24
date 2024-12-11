from utils import read_columns

# Find the total distance between two columns of location IDs
# 1. Sort the columns from smallest to largest
# 2. Compare the columns, and find the difference between each pair
# 3. Sum the differences
def main():
    # Read the columns from the input file
    column1, column2 = read_columns("input.txt")

    # Sort the columns
    column1.sort()
    column2.sort()

    # Find the total distance between the columns
    distance = 0
    for i in range(len(column1)):
        distance += abs(int(column1[i]) - int(column2[i]))
    
    print("Total distance:", distance)
    

if __name__ == "__main__":
    main()