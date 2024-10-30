# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/30/2024
# Description: write a function that take a text that contains a list of numbers, sum and write the values in text.
def file_sum(filename):
    """
    Reads a file containing numbers and returns the sum of the numbers to a text file named sum.txt.
    """
    total = 0

    try:
        # Open the input file and read numbers
        with open(filename, 'r') as file:
            for line in file:
                # Convert each line to a float and add to the total sum
                total += float(line.strip())

        # Write the result to 'sum.txt'
        with open('sum.txt', 'w') as output_file:
            output_file.write(f"{total}\n")

    except FileNotFoundError:
        print(f"File {filename} not found.")
    except ValueError:
        print("One or more lines int the file could not be converted to a number.")