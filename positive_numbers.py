def get_positive_numbers():
    """
    :return: list of the positive numbers the user has entered
    """
    numbers = input("Please enter a sequence of numbers seperated by comma:")
    return list(filter(lambda number: int(number) > 0, numbers.split(",")))


print(get_positive_numbers())
