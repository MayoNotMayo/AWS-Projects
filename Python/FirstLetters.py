#A program that prints the first letters of a sentence input from the user
string = input("Please type in a sentence:")
space = " "

while space in string:
    print(f"{string[0]}")
    index = string.find(space)
    string = string[index + 1:]
print(f"{string[0]}")