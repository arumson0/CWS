from scipy.optimize import fsolve
import math

def equations(p):
    x, y, z, w, u = p
    return (4 + (z/(u*x))*50*(-63),
            -5 + (z/(u*x))*20*(-31),
            0 + (z/(u*x))*13*(-1) + (w/y)*(12 * 26),
            -1 + (z/(u*x))*15*(-1) + (w/y)*(50 * 100),
            -5 + (z/(u*x))*8*(-1)  + (w/y)*(80 * 160)
            )

# fsolve returns a tuple, so you can unpack it directly
x, y, z, w, u = fsolve(equations, (1, 1, 1, 1, 1))

# Print the results
print(equations((x, y, z, w, u)))  # Pass the unpacked tuple as a single argument
