import numpy as np

# Create a structured array
my_structured_array = np.array([('Alice', 25, 65.0), ('Bob', 30, 70.0), ('Carol', 28, 55.0)], dtype=[('name', '<U10'), ('age', '<i4'), ('weight', '<f4')])

# Select rows from the structured array where the age is greater than 28
people_over_28 = my_structured_array[my_structured_array['age'] > 28]

# Print the selected rows
print(people_over_28)
