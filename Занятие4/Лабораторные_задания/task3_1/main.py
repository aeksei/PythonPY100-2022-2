def get_count_char(str_: str) -> dict:

    str_ = ...  # TODO для начала нужно перевести текст в нижний регистр и не забыть что возвращается копия
    char_dict = {}  # словарь для подсчета количества символов

    for char in str_:
        if ...:  # TODO с помощью метода строк isalpha будем проверять, является ли символ буквой
            if ...:  # TODOпроверяем есть ли уже символ среди ключей
                ...  # TODO если есть, то увеличиваем значение на 1
            else:
                ...  # TODO в противном случае создаем новый элемент в словаре
    return char_dict


def frequency_chars(char_dict: dict) -> dict:
    total_count = ...  # TODO найти сумму всех значений словаря

    return ...  # TODO с помощью dict comprehension возвращаем словарь с процентными соотношениями значений


if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
    chars_counter = get_count_char(main_str)
    print(frequency_chars(chars_counter))
