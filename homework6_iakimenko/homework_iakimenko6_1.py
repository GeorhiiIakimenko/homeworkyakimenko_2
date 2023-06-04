def convert_to_float(value):  # Create a function
    try:
        result = float(value)  # In this function, we use a try-except block to catch errors
    except (ValueError, TypeError):  # If a ValueError or TypeError occurs, we set result to 0. Otherwise, if the
        # conversion succeeds, result gets the value of the converted float.
        result = 0
    return result


# Checking the operation of the function code
print(convert_to_float(15))
print(convert_to_float("56.65"))
print(convert_to_float("Function"))
