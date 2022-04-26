def full_names(first_names, last_names, min_length=1):
    """
    :param list first_names: list of strings containing first names.
    :param list last_names: list of strings containing last names.
    :param int min_length: minimum string length for first name + last name
    :return: All the different combinations of first name and last name
             with the minimum length provided
    """
    full_names_variations = [first_name.capitalize() + " " + last_name.capitalize() for first_name in first_names
                             for last_name in last_names if len(first_name) + len(last_name) + 1 >= int(min_length)]
    return full_names_variations


# drive code to test the above function
some_first_names = ['avi', 'moshe', 'yaakov']
some_last_names = ['cohen', 'levi', 'mizrahi']
print(full_names(some_first_names, some_last_names, 10))
print(full_names(some_first_names, some_last_names))
