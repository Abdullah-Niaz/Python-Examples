# In this example, you will learn to check whether a number entered by the user is positive, negative or zero. This problem is solved using if...elif...else and nested if...else statement.

num = int(input("Enter a Number: "))
if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")
