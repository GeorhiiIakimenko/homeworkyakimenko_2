lst1 = [16, 2.5, 3, True, 3.6, 5, '6', 7, 8, 'Python', 9, 0, 'Hillel', 78, False]

lst2 = []  # Create an empty list to store the values
for number in lst1:
    if isinstance(number, (int, float)) and not isinstance(number, bool):  # We use the isinstance function to check
        # if the item is an instance of int or float
        lst2.append(number)  # Add the number to lst2 if it is an instance of int or float, and not isinstance of bool

print(lst2)
