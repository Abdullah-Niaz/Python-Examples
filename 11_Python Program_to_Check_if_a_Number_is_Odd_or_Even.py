# In this example, you will learn to check whether a number entered by the user is even or odd.
# A number is even if it is perfectly divisible by 2. When the number is divided by 2, we use the remainder operator % to compute the remainder. If the remainder is not zero, the number is odd.

n = int(input("Enter the Number "))

if n % 2 == 0:
    print("The Given Number is Even")
else:
    print("Odd Number ")
