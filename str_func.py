def capitalize_words(string):
  """
  Преобразует первые буквы каждого слова в строке в верхний регистр.

  Args:
    string: Строка для преобразования.

  Returns:
    Строка с заглавными первыми буквами каждого слова.
  """

  return ' '.join(word.capitalize() for word in string.split())