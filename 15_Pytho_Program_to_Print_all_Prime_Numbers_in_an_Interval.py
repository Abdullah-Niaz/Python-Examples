# In this program, you'll learn to print all prime numbers within an interval using for loops and display it.

# A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.

# 2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. But 6 is not prime (it is composite) since, 2 x 3 = 6.
# Python program to display all the prime numbers within an interval

for num in range(10, 100):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
