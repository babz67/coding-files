"""
Program to check if a number is odd or even

Note: Enter only whole numbers
"""


num = int(input("Enter a whole number: "))

if num == False or num ==True:
    print(f"{num} is neither odd nor even")
else:
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
