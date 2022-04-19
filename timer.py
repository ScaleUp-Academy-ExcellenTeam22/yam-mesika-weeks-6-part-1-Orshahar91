import time


# Calculates the time it takes for the function to run with the arguments
def timer(function, *args, **kwargs):
    start_timer = time.time()
    print(function(*args, **kwargs))
    end_timer = time.time()
    time_lapsed = end_timer - start_timer
    return time_lapsed
