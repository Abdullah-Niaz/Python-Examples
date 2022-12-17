# In this program, you'll learn to convert Celsuis to Fahrenheit and display it.
# In the program below, we take a temperature in degree Celsius and convert it into degree Fahrenheit. They are related by the formula:
# Formula
# fahrenheit = celsius * 1.8 + 32
# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
# celsius = 37.5
celsius = float(input("Enter the Value of Celcius "))

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('{0} degree Celsius is equal to {1} degree Fahrenheit'.format(
    celsius, fahrenheit))
