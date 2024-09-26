import os
from audioop import reverse
from os.path import split

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    wrong_article = get_wrong_article()

    # Ваш код ниже, возвращайте уже отредактированный текст!
    split_article = wrong_article.splitlines()
    correct_sentence = ''
    correct_article = ''
    for sentence in split_article:
        sentence_without_exc_marks = sentence[:len(sentence)//2].lower()[::-1]
        split_sentence = sentence_without_exc_marks.split()
        for word in split_sentence:
            find_woof = word.find("woof-woof")
            if find_woof == -1:
                correct_sentence = correct_sentence + word + ' '
            else:
                correct_sentence = correct_sentence + word[:find_woof] + 'cat' + word[find_woof + 9:] + " "
        correct_article = correct_article + correct_sentence[:len(correct_sentence)-1].capitalize() + SPLIT_SYMBOL
        correct_sentence = ''
    return correct_article