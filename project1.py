# verb1 = input("enter a verb: ")
# verb2 = input("enter another verb: ")
# adj = input("enter a adjective: ")
# name = input("enter a famous personality: ")
# madlib = f"I like to do {verb1} with my friend {name}  I am very {adj} when it comes to {verb2}."
# print(madlib)

from samples import adventure, kitchen, techtalk
import random

if __name__ == "__main__":
    m = random.choice([adventure, kitchen, techtalk])
    m.madlib()


