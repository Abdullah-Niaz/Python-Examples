# This program displays the multiplication table of variable num (from 1 to 10).
# Multiplication table (from 1 to 10) in Python

# Take input from the user
num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
