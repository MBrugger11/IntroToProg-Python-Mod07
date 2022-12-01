# ------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstration of Pickling and Structured Error Handling
# ChangeLog: (Who, When, What)
# Mark Brugger,11/27/2022,Created Script
# ------------------------------------------------- #

import pickle #importing the pickling function for storing data in binary format

# -- Data -- #
str_file_name = 'AppData.dat'
lst_animal = []


# -- Processing -- #
def read_data_from_file(file_name):
    """ Reads data from a file into a list of dictionary rows

    :param file_name: (string) with name of file:
    :return: (list) of dictionary rows
    """

    file = open(file_name, "rb")
    file_data = pickle.load(file)
    file.close()
    return file_data

def save_data_to_file(file_name, animals):
    """ Writes data from a list of dictionary rows to a File

    :param file_name: (string) with name of file:
    :param animals: (list) you want filled with file data:
    :return: (list) of dictionary rows
    """

    file = open(file_name, "wb")  # wb is used instead of the typical w because we are working with a binary file
    pickle.dump(animals, file)
    file.close()
    print("\n" + "*" * 25)
    print("Your data has been saved!")
    print("*" * 25)
    return animals

# -- Presentation (I/O) -- #

# The first part of the main section of the script will go over simple error handling
#
# obj_file = open("readme.txt", "r")
# If the comment # is removed from the line above and readme.txt does not already exist in the local folder
# Python will fail due to a runtime error (No such fire or directory).
#
# Instead, a simple try/except loop is used to catch this error
try:
    obj_file = open("readme.txt", "r")

except:
    print("\n" + "*" * 80)
    print("readme.txt does not currently exist. It will be created by the program later.")
    print("*" * 80)

# Next, the script will show a simple demonstration of pickling
# Pickling saves data in binary format, rather than in a text format
# The binary file (without some work) is not readable outside of Python

str_name = input("\n\tEnter the name of an animal: ")
int_quantity = int(input("\tEnter the quantity of this animal: "))

# Now the information will be combined into a list

lst_animal = [str_name, int_quantity]

# Using the save_data_to_file function, the list is placed in a binary file.

save_data_to_file(str_file_name,lst_animal)

# Next, the binary file will be read into memory

lst_file = read_data_from_file(str_file_name)
print("\n\b")
print(lst_file)

# For the final section of the script, we will look at error handling and pickling together

try:
    obj_file = open("AppData23.dat", "rb")

    obj_file_data = pickle.load(obj_file)

    int_first = int(input("\n\tEnter a number: "))
    int_second = int(input("\tEnter a second number: "))

    str_math = str(23 * int_first + 11.5 / int_second)

    print("\nNow we will solve the equation 23 * X + 11.5 / Y, where X is your first number and Y is the second.")

    print("The answer is " + str_math)

    print("\nThe last time the script was run, the following data was saved: ")
    print("The first two numbers were the numbers chosen and the last number is the answer to the math operation.")

    print(obj_file_data)

    lst_nums = [int_first, int_second, str_math]

    obj_file = open("AppData23.dat", "wb")

    pickle.dump(lst_nums, obj_file)

    obj_file.close()

except FileNotFoundError as e:  # e is a generic variable. Anything can be used, but typical to use an e for errors
    # This first exception is checking to see if the data file we wish to open already exists.  If it does not,
    # Python will have a run-time error and terminate unexpectedly with an error message that isn't user friendly.

    print("\nFile \"AppData23.dat\" must exist before running this code.")
    print("Built in Python error info: ")
    print(e, e.__doc__, type(e), sep="\n")

except ZeroDivisionError as e:
    # This second exception is for situations where the user's choice of a second number is causing Python
    # to divide by zero

    print("The selection of 0 as your second number has caused the script to divide by zero, which is not allowed.")
    print("Built in Python error info: ")
    print(e, e.__doc__, type(e), sep="\n")

except Exception as e:
    # This final exception is a catch-all for all the other errors that didn't fall into the two categories above
    # You can write as many exception categories as you want to have as many specific error responses as possible
    # but this script demo will limit itself to three.

    print("There was a non-specific error!")
    print("Built in Python error info: ")
    print(e, e.__doc__, type(e), sep="\n")