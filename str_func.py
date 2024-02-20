def str_to_uppercase(string):
    return string.upper()


def capitalize_words(string):
    """
    Функция принимает на вход строку и возвращает ее с заглавными первыми буквами каждого слова.

    Args:
        string (str): Входная строка.

    Returns:
        str : Строка с заглавными первыми буквами каждого слова.
    """
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)