"""
    using sys module
    class Student:
        methods = initialize, checking scores, average_score
"""

from statistics import mean
import sys


class Student:

    def __init__(self):
        # I use self.scores_list beacuse I want create a new list for each object
        self.scores_list = []

    def validate_score(self):
        """check scores for being float positive and then append"""
        for each_num in sys.argv[1:]:
            # using [1:] beacuse first parameter of mentioned list is the address of file
            try:
                # if the number didn't change to float then we get valueerror
                each_num = float(each_num)
                # using assert instead of if , for checking our numbers to being positive
                assert float(each_num) >= 0
                self.scores_list.append(each_num)
            except ValueError:
                return "{}, please write a number".format(ValueError)
            except AssertionError:
                return "{},please write a positive score".format(AssertionError)

    def average_score(self):
        # executing validate_score function to filling the list of scores
        self.validate_score()
        # using statistics method for calculating the average score
        average_score = mean(self.scores_list)
        return average_score


stdn_1 = Student()
print(stdn_1.average_score())
