def vowel_filter(function):
    def wrapper():
        letters = function()
        vowels = 'aoeiuy'
        get_vowels = [char for char in letters if char in vowels]
        return get_vowels

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
