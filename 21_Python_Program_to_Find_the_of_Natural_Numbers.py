# Sum of natural numbers up to num

num = int(input("Enter Number to Count "))

if num < 0:
    print("Enter Positive Number")
else:
    sum = 0
    while (num > 0):
        sum = sum + num
        num = num - 1
    print("Sum of the {0} is {1}".format(num, sum))
# i = 0
# sum = 0
# while i in range(10+1):
#     sum += i
#     i += 1
#     print("The sum is", sum)
