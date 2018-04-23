from morph_rules import vowels
from morph_rules import consonants
from morph_rules import add_affix_choosing_hard_or_soft


def generate_adjective_forms(word_and_tags: tuple) -> list:
    """функция, генерирующая все формы для прилагательного
    """
    result = []
    result += generate_comparative_adjective(word_and_tags)

    return result


def generate_comparative_adjective(word_and_tags: tuple) -> list:
    """функция, генерирующая 2 варианта сравнительной степени прилагательного
    -рақ /-рек
    -ырақ /-iрек
    или
    -лау/-леу
    -дау/-деу
    """
    word, tags = word_and_tags
    result = []

    # -рақ /-рек
    # -ырақ /-iрек
    if (word[-1] in vowels):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="рақ",
                                                   soft_affix="рек")
    elif (word[-1] in consonants):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ырақ",
                                                   soft_affix="iрек")
    new_tags = tags.copy()
    new_tags["degree_of_comparison"] = "<comp>"
    result.append((new_word, new_tags))

    # -лау/-леу
    # -дау/-деу
    if (word[-1] in vowels):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="лау",
                                                   soft_affix="леу")
    elif (word[-1] in consonants):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="дау",
                                                   soft_affix="деу")
    new_tags = tags.copy()
    new_tags["degree_of_comparison"] = "<comp>"
    result.append((new_word, new_tags))

    return result
