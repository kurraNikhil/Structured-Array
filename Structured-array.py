import numpy as np

# Define a nested datatype
my_nested_dtype = np.dtype([('name', '<U10'), ('age', '<i4'), ('children', np.dtype([('name', '<U10'), ('age', '<i4')]))])

# Create a structured array with the nested datatype
my_structured_array = np.array([('Alice', 25, [('Bob', 5), ('Carol', 3)]), ('Dave', 30, [('Eve', 1)])], dtype=my_nested_dtype)

# Print the structured array
print(my_structured_array)
