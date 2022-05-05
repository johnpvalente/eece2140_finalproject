import subprocess


class Student:
    def __init__(self, name, grades, assignments_so_far):
        """
        :param name: Name of student
        :param grades: List containing all grades in history
        :param assignments_so_far: Counter for how many assignments were graded so far
        """
        self.name = name
        self.grades = grades
        self.assignments_so_far = assignments_so_far

    def auto_grade(self, exp_input, exp_output, path, filename):
        """
        :param exp_input: input for python command
        :param exp_output: expected output
        :param path: file path
        :param filename: file name
        :return: this student's average grade for all assignments so far
        """

        cmd = 'python ' + path + '\\' + filename + " " + str(exp_input)

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, text=True)
        out = (p.communicate()[0])

        # if the expected output is equal to the actual output student gets 100
        if int(exp_output) == int(out):
            self.grades.append(100)

        # if expected and actual outputs are not equal, student gets a zero
        else:
            self.grades.append(0)

        # increment total graded assignments
        self.assignments_so_far += 1

        grade_sum = 0
        for grade in self.grades:
            grade_sum += grade

        # return average grade
        return grade_sum / self.assignments_so_far
