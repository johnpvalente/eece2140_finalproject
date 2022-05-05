import os
import pandas as pd
from pycheck_classes import Student


# find and read csv submissions file from file path
def read_csv(path):
    """
    parameters: file path
    returns: answer key answers, all student answers
    opens all files in a designated folder path and formats the .txt file
    """

    # list containing all answers from each file
    submission = []
    try:
        filelist = os.listdir(path)
        for file in filelist:
            if '.csv' in file:
                submission = file
                break

        df = pd.read_csv(path + "\\" + submission)

    except FileNotFoundError:
        raise Exception(f"Invalid path: {path}. Failed to read file")

    return df


def write_grades(path, gradebook):
    """
    :param path: file path
    :param gradebook: student names and grades
    :return text file containing grades
    """
    with open(path + "\\" + "Grades.txt", 'w') as f:
        f.write("Grades \n \n")
        for stud in gradebook.keys():
            f.write(f"{stud}: {round(gradebook[stud],2)}\n")


def grade_students(path):
    """
    :param path: file path
    :return gradebook: dictionary containing student as key and average grade as value
    """
    # get the dataframe from helper method
    df = read_csv(path)

    # find the number of assignments for each student
    names = df.columns[0]
    students = df[names].unique()
    num_assign = df[df[names] == students[0]].shape[0]

    temp_df = pd.DataFrame(df).to_numpy()

    # initialize empty gradebook
    all_students, gradebook = [], {}
    for i in range(len(temp_df)):
        hw = temp_df[i]

        # since every student has the same number of assignments, a new student
        # should be made every multiple of num_assign
        # i.e. if every student has 3 assignments, we know that for every 3 assignments we construct a new student
        if i % num_assign == 0:
            new_student = Student(hw[0], [], 0)
            all_students.append(new_student)

        # fetch the most recent student
        student = all_students[-1]

        # upgrade grade entry in gradebook for student
        gradebook[hw[0]] = student.auto_grade(hw[1], hw[2], path, hw[3])

    # call write grades function to write calculated grades to text file
    write_grades(path, gradebook)
