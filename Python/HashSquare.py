# Draws a square of hashes based on user input

def hash_square(length):
    print(((("#" * length) + "\n") * length))

hash_square(int(input("Please enter the dimensions of the square (a single integer):")))