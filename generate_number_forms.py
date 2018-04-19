from morph_rules import vowels
from morph_rules import consonants
from morph_rules import add_affix_choosing_hard_or_soft

""" TODO Аффиксы ( Шығыс септiк ):
-нан/-нен
-дан/-ден
-тан/-тен
образуют разделительные (по скольку?) и дробные
числительные:
үштен (по три)
жетiден (по семь) оннан (по десять)
елуден (по пятьдесят) бестен бiр = 1/5 (от пяти одна)
"""


def generate_number_forms(word_and_tags: tuple) -> list:
    """функция, генерирующая все формы для числительного
    """
    result = []
    result += generate_ordinal_numeral(word_and_tags)
    result += generate_collective_numeral(word_and_tags)

    return result


def generate_ordinal_numeral(word_and_tags: tuple) -> list:
    """функция, генерирующая порядковое числительное
    после гласных
        -ншы, -ншi
    после согласных
        -ыншы, -iншi
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
    new_tags = tags.copy()
    new_tags["numeral_type"] = "<ord>"
    result.append((new_word, new_tags))

    return result


# Числительные для образования собирательной формы
one_to_seven = {"бiр": "бiреу",
                "екі": "екеу",
                "үш": "үшеу",
                "төрт": "төртеу",
                "бес": "бесеу",
                "алты": "алтау",
                "жеті": "жетеу"}


def generate_collective_numeral(word_and_tags: tuple) -> list:
    """функция, генерирующая собирательные числительные.
    Работает для 1, 2, 3, 4, 5, 6, 7
    -ау, -еу
    """
    word, tags = word_and_tags
    result = []

    # если число не из диапазоне 1-7, возвращаем пустой список
    if word not in one_to_seven.keys():
        return result
    else:
        new_word = one_to_seven.get(word)
        new_tags = tags.copy()
        new_tags["numeral_type"] = "<coll>"
        result.append((new_word, new_tags))
        return result
