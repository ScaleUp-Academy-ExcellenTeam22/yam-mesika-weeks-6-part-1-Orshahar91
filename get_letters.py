def get_letters():
    """
    :return: # The entire alphabet - lower case and upper case.
    """
    return [chr(lowerCase_letter) for lowerCase_letter in range(ord('a'), ord('z') + 1)] +\
           [chr(upperCase_letter) for upperCase_letter in range(ord('A'), ord('Z') + 1)]


print(get_letters())
