def process_arguments(arg1, arg2):  # Create a function
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):  # In the first condition, we check if both
        # arguments are numeric types (int, float). If this is true, we return their multiplied value using the *
        # multiplication operation.
        return arg1 * arg2
    elif isinstance(arg1, str) and isinstance(arg2, str):  # In the second condition, we check whether both arguments
        # are strings (str). If this is true, we return their combined term using the + concatenation operation.
        return arg1 + arg2
    else:
        return arg1, arg2  # If none of the conditions are met, we return a tuple of these arguments with the help
        # of parentheses (arg1, arg2).


result = process_arguments(5, 40)
print(result)
print(type(result))

result = process_arguments(5, 2.17)
print(result)
print(type(result))

result = process_arguments("Python ", "Works")
print(result)
print(type(result))

result = process_arguments(10, "World")
print(result)
print(type(result))
