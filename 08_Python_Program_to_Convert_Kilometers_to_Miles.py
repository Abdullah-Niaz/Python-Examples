# In this example, we'll learn to convert kilometers to miles and display it.
# Taking kilometers input from the user
kilometers = int(input("Enter value in kilometers: "))

# conversion  from  killo meter to miles
# Mean 1 killometer in miles equal to = 0.621371
conversion_rate = 0.621371

# calculate miles
miles = kilometers * conversion_rate
print("{0} Killometers are equal to {1}".format(kilometers, miles))
