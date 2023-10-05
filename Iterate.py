import numpy as np

# Create a structured array
my_structured_array = np.array([('Alice', 25, 65.0), ('Bob', 30, 70.0)], dtype=[('name', '<U10'), ('age', '<i4'), ('weight', '<f4')])

# Iterate over the structured array
for person in my_structured_array:
    print(person['name'], person['age'], person['weight'])
