def multiply(times):
    def decorator(function):
        def wrapped(*args, **kwargs):
            addition = function(*args)
            result = addition * times
            return result

        return wrapped

    return decorator


@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))
