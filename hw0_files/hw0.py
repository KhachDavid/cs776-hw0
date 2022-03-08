# Note: this is the Python syntax for importing modules
# We sometimes use package as a synonym for module, and formally
# a package is a module with a path on the file system.
# Modules may have submodules, which are delimited with .
# i.e. module.submodule
import argparse, os, sys

# Note: 'as' provides an alias for a module so that you can
# access its functions with syntax like np.mean() instead of numpy.mean()
import numpy as np

np.random.seed(776)

def bin_helper(sorted_column_one, bins):
    bin_indices = np.digitize(sorted_column_one, bins)
    current_bin = 1
    bin_has_changed = True
    for index, number in enumerate(sorted_column_one):
        bin_of_current_number = bin_indices[index]
        if bin_of_current_number != current_bin:
            bin_has_changed = True
            current_bin = bin_of_current_number
        if bin_has_changed:
            print()
            print()
            print(f"The left edge of the bin is {str(bins[current_bin - 1])}")
            print(f"The right edge of the bin is {str(bins[current_bin])}")
            print(f"The items in the current bin {str(current_bin)} are the following")
            print()
            bin_has_changed = False
        print(f"{str(number)} falls in bin {str(bin_of_current_number)} ")


def print_matrix(mtrx):
    rtrn = ""
    for row in mtrx:
        for column in row:
            rtrn += '| ' + str(column) + ' '
        rtrn += '|\n'
    return rtrn
# Note: this is the syntax for Python functions. You do not need to
# specify a return type in advance. Multiple values can be returned
# using tuples such as (value1, value2, value3).
def read_file(input_filename):
    # Note: informally, 'with' statements are used for file reading and
    # writing, among other things. They guarantee that the file is properly
    # closed regardless of whether the code block runs normally or throws
    # an exception. The line below opens the file in read mode and creates
    # a file object.
    with open(input_filename, "r") as in_file:
        # Read the file contents.
        # For normal NumPy data, you can load by np.load.
        # But for practice, you need to read them from plain text here.
        file_content = in_file.read()
        file_list = file_content.splitlines()
        for index, string in enumerate(file_list):
            file_list[index] = np.array(string.split(' '), dtype=float)

    for row in file_list:
        for column in row:
            column = float(column)

    return np.array(file_list)

def hw0_test(input_file, output_file):
    # Note: out is the output file you can write to with the print function.
    with open(output_file, "w") as out:
        #####
        #Part 1: strings
        #####
        # Create variables first_name and last_name with your name.
        first_name = 'David'
        last_name = 'Khachatryan'
        tab = '\t'
        # Create full_name by concatenating the variables with a tab
        # separating them and print it.
        full_name = first_name + tab + last_name
        print(full_name)
        # Transform the full_name string to all uppercase letters and
        # print it.
        uppercase_full_name = full_name.upper()
        print(uppercase_full_name)

        #####
        # Part 2: lists
        #####
        # Initialize a list x with four zeros.
        # Prepend one 1 to the head and append one 1 to the tail. Print x.
        x = [0, 0, 0, 0]
        x.insert(0, 1)
        x.append(1)
        print(x)

        # Set y to be the first four elements of x.
        # Change the second to last element of y to 2. Print y.
        y = x[:4]
        print(y)
        # Calculate the product of the elements in y.
        # Pass (skip over) the element if it is 0.  Print the result.
        product = 1
        for num in y:
            product = product * num if num != 0 else product * 1
        print(product)

        # Note: Python strings can be indexed in the same manner as lists.
        course_str = "Advanced Bioinformatics 776"
        # Print the index of 'B'.
        b = course_str.index('B')
        print("The index of B in string " + course_str + " is " + str(b))
        # Print the number of occurrences of "i" and assign it to variable k.
        k = course_str.count('i')
        print(f"The count of occurences of i in {course_str} is {str(k)}")
        # Print the substring of length k starting with 'B'.
        print(course_str[b : b + k])
        #####
        # Part 3: dictionaries and sets
        #####
        # Note: This is set syntax.
        keys = {"a", "b", "c", "d"}
        # Create a dictionary called hash_map.
        # Map the chararacters a-d to 1-4. Save the mapping in hash_map.
        hash_map = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4
        }
        
        # Check if "e" exists in hash_map. If not, map it to 5.
        if 'e' in hash_map:
            print('e is in the hash map')
        else:
            hash_map['e'] = 5
        
        # Print all key-value pairs in format <key:value> like "a:1".
        for key in hash_map:
            print(f'{key}:{str(hash_map[key])}')
        print()
        # Map "e" to 6.
        hash_map['e'] = 6
        # Print all key-value pairs in format <key:value> like "a:1".
        for key in hash_map:
            print(f'{key}:{str(hash_map[key])}')

        #####
        # Part 4: NumPy arrays
        # 
        # Note: you may write a function print_matrix(matrix, output_file) 
        # to print matrices in the desired format.
        #####
        u = [1, 2, -3]
        v = [3, -2, 1]
        # Convert u and v into NumPy arrays.
        u = np.array(u)
        v = np.array(v)
        # Calculate a, the inner product of u and v. Print a.
        # Hint: a is a scalar.
        a = np.dot(u, v)
        print()
        print(f"The inner product of {str(u)} and {str(v)} is {str(a)}")
        # Calculate B, the outer product of u and v. Print B.
        # Hint: B is a 3 by 3 matrix.  
        b = np.outer(u, v, out=None)
        print(f"The outer product of {str(u)} and {str(v)} is\n{print_matrix(b)}")
        # Calculate C = a * B. Print C.
        c = a * b
        print("\n Matrix c")
        print(c)
        # Create R, a 3 by 3 random matrix. Print R.
        print("\n Random matrix r")
        r = np.random.rand(3, 3)
        print(print_matrix(r))
        
        # Calculate the matrix product RC. Print the result.
        print("\nMatrix product of r and c is: ")
        rc = np.matmul(r, c)
        print(print_matrix(rc))

        # Calculate the matrix product CR. Print the result.
        print("\nMatrix product of c and r is: ")
        cr = np.matmul(c, r)
        print(print_matrix(cr))
        # Calculate the elementwise product of R and C. Print the result.
        print("\nElementwise product of r and c is: ")
        elementwise = np.multiply(r, c)
        print(print_matrix(elementwise))
        #####
        # Part 5: NumPy sorting and binning
        #####
        # Complete the read_file function and call it to
        # read the matrix D from input_file into a NumPy array.
        d = read_file(input_file)
        print("The matrix d is: ")
        print(print_matrix(d))
        # Sort the first column of D in ascending order.
        column_one = d[:, 0]
        print("\nThe first column of matrix d")
        print(column_one)

        print("\nThe sorted version of the first column")
        sorted_column_one = np.sort(column_one)
        print(sorted_column_one)
        # Print the first three values of the sorted list.
        print(sorted_column_one[:3])
        # Assign the sorted values into five bins with equal width.
        bins = [-15, -9, -3, 3, 9, 15]
        # The left edge of the first bin is the min value.
        # The right edge of the last bin is the max value.
        # For each bin, print
        #  1) its left and right edges, and
        #  2) the values that fall inside the bin.
        bin_helper(sorted_column_one, bins)

        # Assign the sorted values into five bins such that each bin 
        # contains the same number of elements.
        # Print the values that fall inside each bin.
        bins = [-15, -2, 1, 5, 10, 15]
        bin_helper(sorted_column_one, bins)
        # Sort the last row of D in descending order.
        sorted_row_last = -np.sort(-d[-1])
        # Print the last three values of the sorted list.
        print(sorted_row_last[-3:])
        ### More practice with lists ###
        # Please assign the 5th element from this list to a variable: [1, 2, 3, 5, 8, 13, 21] and print out th eresult.
        lst = [1, 2, 3, 5, 8, 13, 21]
        fifth = lst[4]
        print(fifth)
        # What is the sum of the numbers in this list? Please assign to a variable.
        a = sum(lst)
        print(a)

def main(args):
    input_file = args.inputfile
    output_file = args.outputfile

    hw0_test(input_file, output_file)


# Note: this syntax checks if the Python file is run as the main program
# and will not execute if the module is imported into a different module.
if __name__ == "__main__":
    # Note: this example shows named command line arguments. See the argparse
    # documentation for positional arguments and other examples.
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    # Note: you can use ' or " for strings.
    parser.add_argument('--inputfile',
                        help='input data file path.',
                        type=str,
                        default='data.txt')
    parser.add_argument('--outputfile',
                        help='output file path.',
                        type=str,
                        default='out.txt')

    args = parser.parse_args()
    # Note: this simply calls the main function above, which we could have
    # given any name.
    main(args)
