# In this program, you'll learn to print the Fibonacci sequence using while loop

# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

# The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms. This means to say the nth term is the sum of (n-1)th and (n-2)th term.

num = int(input("Enter thee Value "))
x = 0
y = 1
z = 0
while (z <= num):
    print(z)
    x = y
    y = z
    z = x + y
