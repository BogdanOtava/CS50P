# https://cs50.harvard.edu/python/2022/psets/0/einstein/

# Speed of light (c) is a constant measured in meters per second
SPEED = 300000000

# Prompts user for input (mass) as an integer (kg)
mass = int(input("m: "))

# Formula to calculate Einstein's equation which outputs energy in Joules
energy = mass * (SPEED ** 2)

print(energy)
