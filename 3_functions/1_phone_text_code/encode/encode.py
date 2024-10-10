def encode_text(text: str) -> str | None:
    """Пишите ваш код здесь."""
    keyboard_dict_swap = {}
    keyboard_dict = {
        '1': ['.', ',', '?', '!', ':', ';'],
        '2': ['а', 'б', 'в', 'г'],
        '3': ['д', 'е', 'ж', 'з'],
        '4': ['и', 'й', 'к', 'л'],
        '5': ['м', 'н', 'о', 'п'],
        '6': ['р', 'с', 'т', 'у'],
        '7': ['ф', 'х', 'ц', 'ч'],
        '8': ['ш', 'щ', 'ъ', 'ы'],
        '9': ['ь', 'э', 'ю', 'я'],
        '0': [' ']
    }
    for key, value in keyboard_dict.items():
        for elem in range(len(value)):
            keyboard_dict_swap[value[elem]] = key * (elem + 1)
    result = ''
    for word in text:
        if word in keyboard_dict_swap:
            result += keyboard_dict_swap[word] + ' '
        else:
            return None
    return result[:-1]