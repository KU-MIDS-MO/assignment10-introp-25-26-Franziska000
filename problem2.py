##Problem 2

# For the parameter value

# \[
# r = 10
# \]

# perform the following tasks;

# - plot the ellipse and the line defined in **Problem 1** in the same coordinate system,
# - plot the intersection points obtained in **Problem 1** as clearly visible markers,
# - label both coordinate axes,
# - choose a sensible plotting range,
# - save the figure as a pdf file named **`Problem2.pdf`**

# This problem will be **graded manually** based on the correctness and clarity of the plot.

# Before committing your submission, make sure to add the pdf file to your repository using;

# git add Problem2.pdf

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

x, y, r = symbols('x y r')

eq1 = Eq(2*x**2 + 3*y**2, r)
eq2 = Eq(y, 2*x + 1)

sol = solve([eq1.subs(r, 10), eq2], [x, y], dict=True)

x_vals = np.linspace(-3, 3, 400)

y_vals_eq1_pos = np.sqrt((10 - 2*x_vals**2) / 3)
y_vals_eq1_neg = -y_vals_eq1_pos
y_vals_eq2 = 2*x_vals + 1

plt.plot(x_vals, y_vals_eq1_pos, label='2x**2 + 3y**2 = 10')
plt.plot(x_vals, y_vals_eq1_neg)
plt.plot(x_vals, y_vals_eq2, label='y = 2x + 1')

x = [float(s[x]) for s in sol]
y = [float(s[y]) for s in sol]

plt.scatter(x, y, color='red', label='Solution Point')

plt.xlabel('x')
plt.ylabel('y')
plt.title('System of Equations')
plt.legend()
plt.grid(True)
plt.show()

pass