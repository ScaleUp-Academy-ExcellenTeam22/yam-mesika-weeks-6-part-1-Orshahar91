import time


def timer(function, *args, **kwargs):
    """
    # Calculates the time it takes for the function to run with the arguments
    :param function: The function to run on the arguments
    :param args: Non keyworded variable length argument list
    :param kwargs: Keyworded variable length of arguments
    :return: The time it takes for the function to finish running the arguments
    """
    start_timer = time.time()
    function(*args, **kwargs)
    end_timer = time.time()
    time_lapsed = end_timer - start_timer
    return time_lapsed
