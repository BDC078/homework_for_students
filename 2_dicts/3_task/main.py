from os.path import split


def format_phone(phone_number: str) -> dict[str, int]:
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+']
    correct_phone_numbers = ''
    for index in range(len(phone_number)):
        if phone_number[index] in numbers:
            correct_phone_numbers += phone_number[index]
    if correct_phone_numbers[0] == '7' or correct_phone_numbers[0] == '8':
        return ('8 (' + correct_phone_numbers[1:4]+') '+correct_phone_numbers[4:7]+'-'+correct_phone_numbers[7:9] +
                '-' + correct_phone_numbers[9:11])
    elif correct_phone_numbers[0] == '+':
        return ('8 ('+correct_phone_numbers[2:5]+') '+correct_phone_numbers[5:8]+'-'+correct_phone_numbers[8:10] +
              '-'+ correct_phone_numbers[10:12])
    elif correct_phone_numbers[0] == '9':
        return ('8 ('+correct_phone_numbers[0:3]+') '+ correct_phone_numbers[3:6]+ '-'+ correct_phone_numbers[6:8]+
              '-'+correct_phone_numbers[8:10])