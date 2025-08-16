"""
Python program to check if a number is positive, negative or zero
"""

num = float(input("Enter your number: "))

if num == False:
    print("It is zero")
else:
    if abs(num) == num:
        print("It is positive")
    else:
        print("It is negative")

    
