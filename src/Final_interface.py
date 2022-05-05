# import function from separate .py file
from text_check import AutoGrader
from py_check_func import grade_students


# function to give instructions and run .txt file auto grader
def text_grade_interface():
    # provide user with formatting instructions
    print("Ensure the answer key is named '0_Answer Key' to ensure it is the first file.")
    print("All student files in the folder should be labeled with their name as follows: 'First Last'")
    print("The answer key should have the format: \n"
          "Answer Key\n"
          "\n"
          "1. Answer\n"
          "2. Answer\n"
          "etc.\n")
    print("The student answers should have the format: \n"
          "FirstName LastName\n"
          "\n"
          "1. Answer\n"
          "2. Answer\n"
          "etc.\n")
    print("Ensure there is no extra line after the last answer in the text files.\n")

    # get folder path from user
    folder_path = input("Please input the path to the folder containing the answer key and student responses,"
                        " without any quotation marks: \n")

    # run function
    AutoGrader.autograder(folder_path)


# function to give instructions and run .py file auto grader
def python_grade_interface():
    print("The folder must contain a .csv file with the students' name, expected input, desired output, and file name.")
    print("The folder must also contain all of the students' .py files.")
    print("Each file name must end in .py")
    print("Each student must have the same number of assignments/programs.")
    print("The folder will compare the desired output to the program output and give a 0% or 100% for each .py file.")
    print("Each student's final grade will be output to a text file called 'Grades.txt'\n")
    folder_path = input("Please input the path to the folder containing the .csv file and python files,"
                        " without quotation marks.\n")

    grade_students(folder_path)


# function to determine which auto grader the user wants and run it
def main_interface():
    print("Are you looking to grade .txt files or .py files?")
    choice = int(input("Enter a 0 for .txt files or a 1 for .py files.\n"))
    if choice == 0:
        text_grade_interface()
    elif choice == 1:
        python_grade_interface()
    else:
        print("Please try again and enter a valid choice.")


main_interface()
