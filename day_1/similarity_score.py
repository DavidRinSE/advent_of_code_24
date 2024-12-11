from utils import read_columns

# Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
# 1. Sort the columns from smallest to largest
# 2. Find the similarity score between the columns
# 3. Sum the similarity scores
def main():
    # Read the columns from the input file
    column1, column2 = read_columns("input.txt")

    # Sort the columns
    column1.sort()
    column2.sort()

    # Find the total similarity score between the columns
    similarity_score = 0
    for i in range(len(column1)):
        similarity_score += int(column1[i]) * column2.count(column1[i])
    
    print("Total similarity score:", similarity_score)

if __name__ == "__main__":
    main()