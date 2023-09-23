"""
    using argparse module
    class Student:
        methods: initialize, average
"""

import argparse
from numpy import mean


class Student:
    
    def __init__(self):
        # create a object from argparse
        self.parser = argparse.ArgumentParser()
        # using required argument to Indicate an argument is required
        self.parser.add_argument(
            '-g', '--grades', help='Your grades', type=float, required=True, nargs='*')
        self.parser.add_argument(
            '-f', '--floats', help='Your floats', type=int, required=False, default=2)
        self.args = self.parser.parse_args()

    def get_average(self):
        # Using the round function to calculate the average with a certain decimal value
        Average = round(mean(self.args.grades), self.args.floats)
        return Average


stdn_1 = Student()
print(stdn_1.get_average())


# nargs stands for Number Of Arguments:
# 3: 3 values, can be any number you want
# ?: a single value, which can be optional
# *: a flexible number of values, which will be gathered into a list
# +: like *, but requiring at least one value
