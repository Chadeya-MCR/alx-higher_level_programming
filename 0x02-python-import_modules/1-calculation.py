# main.py

# Define variables a and b
a = 10
b = 5

# Import functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Perform mathematical operations and print results
result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

# Display results
print("{} + {} = {}".format(a, b, result_add))
print("{} - {} = {}".format(a, b, result_sub))
print("{} * {} = {}".format(a, b, result_mul))
print("{} / {} = {}".format(a, b, result_div))
