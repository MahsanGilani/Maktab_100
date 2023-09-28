"""
    modules= argparse
    class 
"""
import argparse
import os
from pathlib import Path

class Sized:
    
    def __init__(self):
        # create a object from argparse
        self.parser = argparse.ArgumentParser()
        self.group = self.parser.add_mutually_exclusive_group(required=True) #https://www.programming-books.io/essential/python/setting-mutually-exclusive-arguments-with-argparse-2fef841b30d04aa68b38f700fe3d830e
        self.group.add_argument('-d', '--directory', help='directory address',type=str)
        self.group.add_argument('-f', '--file', help='file address',type=str)
        # self.parser.add_argument('-F', '--Format', help='file format', type=str)
        self.args = self.parser.parse_args()
    
    def directory_size(self): 
        # az in site fahmidam https://www.geeksforgeeks.org/how-to-get-size-of-folder-using-python/
        size=0
        for path, dirs, files in os.walk(self.args.directory):  # متد والک یه تاپل برمیگردونه که داخلش سه تا مقدار وجود داره
            for f in files:
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)

        return str(size/1000) # Baraye kb shodan taghsim kardam
    
    def file_size(self):
        file_size = os.path.getsize(self.args.file)
        return file_size/1000
    
    def check_which_one(self):
        if self.args.directory:
            return self.directory_size()
        elif self.args.file:
            return self.file_size()
    # def directory_size(self): # https://snipplr.com/view/47686/python-recursive-get-size-of-directory
    #     total_size = os.path.getsize(self.args.directory)
    #     for item in os.listdir(self.args.directory):
    #         itempath = os.path.join(self.args.directory, item)
    #         if os.path.isfile(itempath):
    #             total_size += os.path.getsize(itempath)
    #         elif os.path.isdir(itempath):
    #             total_size += self.directory_size()
    #     return total_size

obj1=Sized()

print(obj1.check_which_one())


#https://virgool.io/@mce.armankarimi/%D9%85%D8%AA%D8%AF-oswalk-n4i733lvhlsp