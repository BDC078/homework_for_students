def decode_numbers(numbers: str) -> str | None:
    """Пишите ваш код здесь."""
    result = ''
    list_numbers = numbers.lower().split()
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
    for code in list_numbers:
        if (((code[0] == '1') and len(code) <= 6) or ((code[0] in ['2', '3', '4', '5', '6', '7', '8', '9'])
                                                      and len(code) <= 4)
            or ((code[0] == '0') and len(code) <= 1)) and (code[0] == code[-1]):
            result += keyboard_dict[code[0]][len(code) - 1]
        else:
            result = None
            break
    return result