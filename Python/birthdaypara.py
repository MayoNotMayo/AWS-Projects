#A short program to demonstrate the birthday paradox
x = 365
y = 365
prop = 1
people = int(input("How many people are there?"))

while y != 365 - people:
    prop *= (y/x)
    y -= 1

print(f"There is a {100 - (prop * 100)}% chance that 2 people share the same birthday.")