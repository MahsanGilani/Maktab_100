"""
    class Game:
        methods = initialize (kolle chizmizaye argparse), pc_guess, check_user_guess
"""
import argparse
import random

class Game:
    
    def __init__(self):
        # create a object from argparse
        self.parser = argparse.ArgumentParser()
        # using required argument to Indicate an argument is required
        self.parser.add_argument('-s', '--start', help='adade shoru shavande baraye range random', type=int, required=True)
        self.parser.add_argument('-e', '--end', help='adade tamam konande baraye range random', type=int, required=True)
        self.parser.add_argument('-g', '--guess', help='faghat ta chand bar hads', type=int, required=True, default=5)
        self.args = self.parser.parse_args()

    def pc_guess(self):
        # Using the round function to calculate the average with a certain decimal value
        cmptr_guess = random.randint(self.args.start,self.args.end)
        return cmptr_guess
    
    def check_guess(self):
        computer_guess = Game.pc_guess(self)
        while True:
            for _ in range(self.args.guess):
                user_input=int(input("please enter your guess: "))
                if user_input>computer_guess:
                    print("Enter smaller guess")
                elif user_input<computer_guess:
                    print("Enter bigger guess") 
                else:
                    print("Yesss tou win the game!!!!")
                    break
            else:
                print("oh you lost the game!!! try again later...")
                # break
                

       
obj1=Game()
# print(obj1.check_guess())
obj1.check_guess()
        
   
