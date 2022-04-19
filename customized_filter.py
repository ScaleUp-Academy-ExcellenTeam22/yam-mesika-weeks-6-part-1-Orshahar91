# Customized filter to act as regular built in filter
def my_filter(function, iterable):
    filtered_list = []
    for value in iterable:
        if function is not None:
            if function(value):
                filtered_list.append(value)
        else:
            if value:
                filtered_list.append(value)
    return filtered_list


# driver code to test the above function
def is_mature(age):
    return age >= 18


to_sum = [(1, -1), (2, 5), (5, -3, -2), (1, 2, 3)]
sum_is_not_zero = my_filter(sum, to_sum)
print(tuple(sum_is_not_zero))

to_sum = [0, "", None, 0.0, True, False, "Hello"]
equivalent_to_true = my_filter(None, to_sum)
print(tuple(equivalent_to_true))

ages = [0, 1, 4, 10, 20, 35, 56, 84, 120]
mature_ages = my_filter(is_mature, ages)
print(tuple(mature_ages))
