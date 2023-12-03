def tags(html_tag):
    def decorator(function):
        def wrapper(*args):
            result = function(*args)
            return f'<{html_tag}>{result}</{html_tag}>'

        return wrapper

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
