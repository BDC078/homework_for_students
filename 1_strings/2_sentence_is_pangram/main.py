"""
Панграмма - предложение, которое использует каждую букву алфавита (в нашем случае - английского алфавита).
Необходимо реализовать код, который скажет, является предложение панграммой или нет.
Буквы в верхнем и нижнем регистрах считаются эквивалентными.
Предложения содержат только буквы английского алфавита, без пробелов и т.п.
Проверка:
pytest ./2_sentence_is_pangram/test.py
"""
import string

def is_sentence_is_pangram(sentence: str) -> bool:
    """Пишите ваш код здесь."""
    character_of_sentence = set(char for char in sentence.lower())
    alphabet = {char gitfor char in string.ascii_lowercase}
    if character_of_sentence == alphabet:
        return True
    else:
        return False