#The quadratic formula using sqrt function
from math import sqrt

vara = float(input("Value of a:"))
varb = float(input("Value of b:"))
varc = float(input("Value of c:"))

posrt = (-varb + sqrt(varb**2 - 4*vara*varc))/(2*vara)
negrt = (-varb - sqrt(varb**2 - 4*vara*varc))/(2*vara)

print(f"The roots are {posrt} and {negrt}")
# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5