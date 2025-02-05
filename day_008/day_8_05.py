#  Exercise 50:Roots of aQuadraticFunction
#  (24 Lines)
#  Aunivariate quadratic function has the form f (x) = ax2 + bx + c, where a, b and
#  c are constants, and a is non-zero. The roots of a quadratic function can be found
#  by finding the values of x that satisfy the quadratic equation ax2 + bx + c = 0. A
#  quadratic function may have 0, 1 or 2 real roots. These roots can be computed using
#  the quadratic formula, shown below:
#  √
#  root = −b±
#  b2 −4ac
#  2a
#  Theportion ofthe expression under the square root sign is called the discriminant.
#  If thediscriminantisnegativethenthequadraticequationdoesnothaveanyrealroots.
#  If the discriminant is 0, then the equation has one real root. Otherwise the equation
#  has two real roots, and the expression must be evaluated twice, once using a plus
#  sign, and once using a minus sign, when computing the numerator.
#  Writeaprogramthatcomputestherealrootsofaquadraticfunction.Yourprogram
#  shouldbeginbypromptingtheuserforthevaluesofa,b andc.Thenitshoulddisplay
#  a message indicating the number of real roots, along with the values of the real roots
#  (if any)

import math

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("The quadratic equation has no real roots.")
elif discriminant == 0:
    root = -b / (2*a)
    print("The quadratic equation has one real root:", root)
else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The quadratic equation has two real roots:", root1, "and", root2)