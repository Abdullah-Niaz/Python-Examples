# In this program, you'll learn to calculate the area of a triangle and display it.
# Python Program to find the area of triangle

a = 5 # first Side
b = 6 #Second Side
c = 7 #Third Side
# calculate the semi-perimeter
s = (a + b + c) / 2
# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is ', area)