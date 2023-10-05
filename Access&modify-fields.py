import numpy as np

# Create a structured array
my_structured_array = np.array([('Alice', 25, 65.0), ('Bob', 30, 70.0)], dtype=[('name', '<U10'), ('age', '<i4'), ('weight', '<f4')])

# Access a field of the structured array
print(my_structured_array['name'])

# Modify a field of the structured array
my_structured_array['weight'] = my_structured_array['weight'] * 2.20462

# Print the structured array
print(my_structured_array)
