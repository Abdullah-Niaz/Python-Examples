# In this program, you'll learn to find the largest among three numbers using if else and display it.
# In the program below, the three numbers are stored in num1, num2 and num3 respectively. We've used the if...elif...else ladder to find the largest among the three and display it.

a = int(input("Enter the First Value "))
b = int(input("Enter the Second Value "))
c = int(input("Enter the Third Value "))

if (a > b and a > c):
    print("{0} is Greater".format(a))
elif (b > c):
    print("{0} is Greater".format(b))
else:
    print("{0} is Greater".format(c))
