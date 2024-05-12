"""
A flawed VowelCounter that only excludes lower case letters
but also counts special characters any upper case letters.
"""

txt = str(input())

x = ""
y = ""
z = "bcdfghjklmnpqrstvwxyz"

mytable = str.maketrans(x, y, z)


print(len(txt.translate(mytable).replace(" ", "")))