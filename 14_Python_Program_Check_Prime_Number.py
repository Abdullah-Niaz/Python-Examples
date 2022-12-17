# Example to check whether an integer is a prime number or not using for loop and if...else statement. If the number is not prime, it's explained in output why it is not a prime number.

# A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number. 2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. But 6 is not prime (it is composite) since, 2 x 3 = 6.

num = int(input("Enter the Value to Check Prime Numbers "))
for i in range(2, num):
    if num % i == 0:
        print(num, "is not prime number")
        break
else:
    print(num, "It's Prime Number")
