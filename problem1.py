##Problem 1

# Consider the system of equations

# \( 2x^2 + 3y^2 = r \) and \( y = 2x + 1 \)

# where \( r \) is a real parameter

###your task;

# Write your code  using **SymPy** that:

# -defines the symbolic variables `x`, `y`, and `r`,
# - symbolically solve the system for `x` and `y`,
# - stores **all solutions** in a list named `sol`,
# - where each element of `sol` is a dictionary mapping
#   `{x: ..., y: ...}` in terms of the parameter `r`.

# x, y unknowns; r parameter

# Your solution must be **fully symbolic** and must not substitute a numerical value for `r` in this problem.

import sympy as sp
from sympy import symbols, Eq, solve

x, y, r = symbols('x y r')

eq1 = Eq(2*x**2 + 3*y**2, r)
eq2 = Eq(y, 2*x + 1)

sol = solve([eq1, eq2], [x, y], dict=True)

print(sol)

pass
