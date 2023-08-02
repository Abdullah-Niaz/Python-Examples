# he decimal system is the most widely used number system. However, computers only
# understand binary. Binary, octal and hexadecimal number systems are closely related,
# and we may require to convert decimal into these systems.

# The decimal system is base 10 (ten symbols, 0-9, are used to represent a number) and similarly,
# binary is base 2, octal is base 8 and hexadecimal is base 16.
# A number with the prefix 0b is considered binary, 0o is considered octal and 0x as hexadecimal.

# Python program to convert decimal into other number systems
dec = 60

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
