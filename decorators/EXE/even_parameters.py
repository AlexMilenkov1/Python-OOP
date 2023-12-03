def even_parameters(function):
    def wrapper(*args):
        if all(isinstance(el, int) and el % 2 == 0 for el in args):
            return function(*args)
        return 'Please use only even numbers!'

    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))
