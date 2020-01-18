# Exercise 1
# source: https://www.practicepython.org/
from datetime import date

name = input("Tell me your name: ")
age = int(input("Now, tel me your age: "))
year = 2020
birthdayYear = year - age
print("Accordin to the given age I estimaded that you were born in ",birthdayYear)

#date = 
print("Your 100-birthday year was estimaded according to the given age.")
choose = input("Would you like me to print it (Y/N?)")

if choose == "Y":
    print("It will be in", birthdayYear + 100)
elif choose == "N":
    print("That is OK. The program will be terminated now.")
