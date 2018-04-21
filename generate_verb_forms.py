from morph_rules import vowels
from morph_rules import voiced_consonants
from morph_rules import voiceless_consonant
from morph_rules import add_affix_choosing_hard_or_soft


def generate_verb_forms(word_and_tags: tuple) -> list:
    """функция, генерирующая все формы для глагола
    """
    result = []
    result += generate_negative_verb(word_and_tags)

    return result


def generate_negative_verb(word_and_tags: tuple) -> list:
    """функция, генерирующая отрицательную форму глагола
    после гласных и Р, Л
        –ма/-ме
    после звонких и М, Н
        –ба/-бе
    после глухих
        –па/-пе
    """
    word, tags = word_and_tags
    result = []

    if (word[-1] in vowels) \
            or (word[-1] in ['р', 'л']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ма",
                                                   soft_affix="ме")
    elif (word[-1] in voiced_consonants) \
            or (word[-1] in ['м', 'н']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ба",
                                                   soft_affix="бе")
    elif (word[-1] in voiceless_consonant):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="па",
                                                   soft_affix="пе")
    new_tags = tags.copy()
    new_tags["negativity"] = "<neg>"

    result.append((new_word, new_tags))
    return result
