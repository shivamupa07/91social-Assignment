dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make':'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

print("Original list of dictionaries :")
print(dict)

sorted_dict = sorted(dict, key = lambda x: x['color'])

print("\nSorting the List of dictionaries :")
print(sorted_dict)