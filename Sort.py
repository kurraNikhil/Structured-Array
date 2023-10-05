import numpy as np

# Create a structured array
my_structured_array = np.array([('Alice', 25, 65.0), ('Bob', 30, 70.0), ('Carol', 28, 55.0)], dtype=[('name', '<U10'), ('age', '<i4'), ('weight', '<f4')])

# Sort the structured array by age
my_structured_array.sort(order='age')

# Print the sorted structured array
print(my_structured_array)
