# import os library for file and folder reading
import os


class AutoGrader:

    @staticmethod
    def format_text_file(txt_file):
        """
        parameter: txt file
        return: list
        """

        # file formatting
        file = txt_file.readlines()
        temp = []
        for line in file:
            temp.append(line.replace("\n", ""))

        stud_name = temp[0]
        temp = temp[2:]

        lines = []
        for i in temp:
            lines.append(i.split())

        for j in range(len(lines)):
            lines[j] = lines[j][1]

        # add the name to identify responses
        lines.insert(0, stud_name)

        return lines

    @staticmethod
    def open_files(path):
        """
        parameters: file path
        returns: answer key answers, all student answers
        opens all files in a designated folder path and formats the .txt file
        """

        # list containing all answers from each file
        all_files = []
        try:
            filelist = os.listdir(path)
        except:
            raise FileNotFoundError

        for file in filelist:

            # ignore the grades file being written to
            if file != "Grades.txt":
                with open(path + "\\" + file) as f:
                    all_files.append(AutoGrader.format_text_file(f))

        # the answer key is the first element
        ans = all_files[0]

        # remove the answer key from the student responses
        all_files.pop(0)
        all_answers = all_files

        return ans, all_answers

    @staticmethod
    def grader(ans_key, student):
        """
        parameters: two lists
        returns: float
        """

        correct = 0

        # range is from 1 to the end of the list to skip the names
        for i in range(1, len(list(ans_key))):

            if ans_key[i] == student[i]:
                correct += 1

        return (correct / (len(ans_key) - 1)) * 100

    @staticmethod
    def autograder(path):
        """
        parameters: file path
        returns: .txt file with all student grades out of 100
        """

        # gets correct answers and student answers from open_files function
        answer_key, student_answers = AutoGrader.open_files(path)
        answer_key = answer_key

        # writes students final grades to text file in folder
        with open(path + "\\" + "Grades.txt", 'w') as f:
            f.write("Grades \n \n")
            for student in student_answers:
                score = AutoGrader.grader(answer_key, student)
                f.write(f"{student[0]}: {score} \n")
