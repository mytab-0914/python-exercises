# TASK: Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.

print("The program evaluates given number if it is ODD, or EVEN.")

num = int(input("Enter a number: "))


if num % 2 == 0:
    print("Given number is EVEN")

else:
    print("Given number is ODD")
