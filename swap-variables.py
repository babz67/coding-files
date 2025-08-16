"""
Python program to swap two variables

Initially two variables contain numbers 1 and 2
After swapping, they should contain 2 and 1
"""

var1 = 1
var2 = 2
print(f"Before swapping: var1 contains {var1} and var2 contains {var2}")
var1,var2 = var2,var1
print("Swapped")
print(f"After swapping: var1 contains {var1} and var2 contains {var2}")
