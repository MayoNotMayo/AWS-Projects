"""
A flawed VowelCounter that only excludes lower case letters
but also counts special characters any upper case letters.
"""

#take user string input
txt = str(input())

#z is used to remove characters from the input
x = ""
y = ""
z = "bcdfghjklmnpqrstvwxyz"

#assigns mytable to the translation of txt
mytable = str.maketrans(x, y, z)

#prints the length of txt after deleting the spaces from txt
print(len(txt.translate(mytable).replace(" ", "")))