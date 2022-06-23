# A magic square is a matrix of numbers whose columns, rows, and diagonals all sum to the same number.
# This program reads numbers from a text file and generates a report for each with a conclusion on
# whether or not it is a magic square.


# Opens and begins to organize data from the text file
def open_file():
    with open('magicData.txt') as readfile:
        numbers = readfile.read()
        numbers = numbers.split('\n')    # splits each row of the text file into elements of a list
        return numbers


# Creates dictionary to store each magic square as a 2-dimensional list. The keys are the numbers 1-7, corresponding to
# the first through seventh squares in the text file. Each row in the square is its own list.
squares = {}
def generate_lists(list):
    i = 0
    for item in list:
        item = item.split()
        if item[0] != '-1':
            if len(item) == 1:    # checks whether number is part of the square or a single number
                i += 1
                squares[i] = []    # creates a list when a new square begins in the text file
            else:                   # adds each row in the square to the list
                squares[i].append(item)


# Takes the key for the square as input and locates the square in the dictionary created above. Loops through each row
# in the square and initializes a variable for each to sum up and then print the number.
def sum_rows(dict_key):
    row_sums = []
    for row in squares[dict_key]:
        row_sum = 0
        for number in row:
            row_sum += int(number)
        print('Sum of row:', row_sum)
        row_sums.append(row_sum)
    return row_sums    # produces a list of the sums to compare later


# Creates a for loop to determine the size of the square and keep summing each column by its list index i until there are
# no columns left.
def sum_columns(dict_key):
    i = 0
    col_sums = []
    while i < len(squares[dict_key]):
        column_sum = 0
        for row in squares[dict_key]:
            column_sum += int(row[i])
        print('Column Sum:', column_sum)
        col_sums.append(column_sum)
        i += 1
    return col_sums    # produces a list of the sums to compare later


# Initializes two variables to check each diagonal and increments forwards one for the first diagonal and backwards one
# for the second diagonal.
def sum_diagonal(dict_key):
    i = 0
    diag_sum_left = 0
    diag_sum_right = 0
    results = []
    for row in squares[dict_key]:
        diag_sum_left += int(row[i])
        diag_sum_right += int(row[len(row) - (i + 1)])    # starts at the end of the list then increments backwards by 1
        i += 1
    print('First diagonal sum:', diag_sum_left)
    print('Second diagonal sum:', diag_sum_right)
    results.append(diag_sum_right)
    results.append(diag_sum_left)
    return results    # produces a list of the sums to compare later


# Formats and prints out information for each square, including the dimensions, the contents of the square, all of the
# sums calculated above, and whether or not it is a magic square
def report_results():
    for i in range(1,8):
        print('The size of the square is:', len(squares[i]))
        print('*****', 'Square', i, '*****')
        for rows in squares[i]:
            for num in rows:
                print(num, end=' ')
            print()
        total_sums = sum_rows(i) + sum_columns(i) + sum_diagonal(i)    # combines row, column, and diagonal sums into one list
        total_sums = set(total_sums)    # removes duplicates from the list of sums by making it into a set
        if len(total_sums) == 1:      # checks whether there was more than one distinct value present in the list
            print('This is a magic square')
        else:
            print('This is not a magic square')
        print()


# Combines and executes the above functions
def main():
    generate_lists(open_file())
    report_results()

main()
