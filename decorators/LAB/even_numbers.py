def even_numbers(function):
    def wrapper(*args, **kwargs):
        current_numbers = function(*args)
        result_even_numbers = [num for num in current_numbers if num % 2 == 0]
        return result_even_numbers

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
