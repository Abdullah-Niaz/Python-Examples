# In this article, you'll learn to find the factorial of a number and display it.

# The factorial of a number is the product of all the integers from 1 to that number.
# For example, the factorial of 6 is 1*2*3*4*5*6 = 720. Factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1.

num = int(input("Enter the Number to Find out the Factorial "))
factorial = 1
if num < 0:
    print("Sorry, Factorial of Negative Number Does'nt Exit ")
elif num == 0:
    print("Factorial of 0 is Zero ")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("Factorial of The {0} is {1}".format(num, factorial))
