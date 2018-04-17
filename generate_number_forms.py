from morph_rules import vowels
from morph_rules import consonants
from morph_rules import add_affix_choosing_hard_or_soft


def generate_number_forms(word_and_tags: tuple) -> list:
    """функция, генерирующая все формы для числительного
    """
    result = []
    return result


def generate_ordinal_numeral(word_and_tags: tuple) -> list:
    """функция, генерирующая порядковое числительное
    после гласных
        - ншы, - ншi
    после согласных
        - ыншы, - iншi
    """
    word, tags = word_and_tags
    result = []

    if len(set(word[-1]).intersection(vowels)) != 0:
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ншы",
                                                   soft_affix="ншi")
    elif len(set(word[-1]).intersection(consonants)) != 0:
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ыншы",
                                                   soft_affix="iншi")
    new_tags = tags + "<ord>"
    result.append((new_word, new_tags))

    return result
