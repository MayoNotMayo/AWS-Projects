"""Final VowelCounter using regex expressions to count the vowels taken from a user's input.
Challenged myself to make it as short as I could and fix my previous mistake from a moment ago when I made VowelCounter.py (also on my GitHub above this file)."""

#import the regex package
import re

"""Using findall, we can search a string input from the user for vowels. 
Using the flag IGNORECASE will ignore the case of the letters, whether they are lowercase or uppercase. 
len will count the occurrences and then print the output."""
print(len(re.findall("a|e|i|o|u", input(), flags=re.IGNORECASE)))
