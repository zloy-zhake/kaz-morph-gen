from morph_rules import vowels
from morph_rules import voiced_consonants
from morph_rules import voiceless_consonant
from morph_rules import add_affix_choosing_hard_or_soft
from common_forms import generate_all_personals


def generate_verb_forms(word_and_tags: tuple) -> list:
    """функция, генерирующая все формы для глагола
    """
    result = []
    result += generate_negative_verb(word_and_tags)
    result += generate_all_zhedel_otken_shaq(word_and_tags)
    result += generate_all_buryngy_otken_shaq_1(word_and_tags)

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


def generate_all_zhedel_otken_shaq(word_and_tags: tuple) -> list:
    """функция, генерирующая жедел өткен шақ во всех лицах
    Основа глагола + -ды/-дi/-ты/-тi + краткие личные окончания
    глухие -ты/-тi
    неглухие -ды/-дi
    """
    word, tags = word_and_tags
    result = []

    if word[-1] in voiceless_consonant:
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ты",
                                                   soft_affix="ті")
    else:
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ды",
                                                   soft_affix="ді")

    # 3 лицо ед. и мн.число генерируется вначале
    # Потом на его основе генерируются остальные лица
    new_tags = tags.copy()
    new_tags["tense"] = "<past><zhedel-otken>"
    new_tags["person"] = "<p3>"
    new_tags["plurality"] = "<sp>"
    result.append((new_word, new_tags))

    # 1 лицо ед.число
    tmp_new_word = new_word + 'м'
    new_tags = tags.copy()
    new_tags["tense"] = "<past><zhedel-otken>"
    new_tags["person"] = "<p1>"
    new_tags["plurality"] = "<sg>"
    result.append((tmp_new_word, new_tags))

    # 1 лицо мн.число
    tmp_new_word = add_affix_choosing_hard_or_soft(new_word,
                                                   hard_affix='қ',
                                                   soft_affix='к')
    new_tags = tags.copy()
    new_tags["tense"] = "<past><zhedel-otken>"
    new_tags["person"] = "<p1>"
    new_tags["plurality"] = "<pl>"
    result.append((tmp_new_word, new_tags))

    # 2 лицо ед.число
    tmp_new_word = new_word + 'ң'
    new_tags = tags.copy()
    new_tags["tense"] = "<past><zhedel-otken>"
    new_tags["person"] = "<p2>"
    new_tags["plurality"] = "<sg>"
    result.append((tmp_new_word, new_tags))

    # 2 лицо мн.число
    tmp_new_word = add_affix_choosing_hard_or_soft(new_word,
                                                   hard_affix='ңдар',
                                                   soft_affix='ңдер')
    new_tags = tags.copy()
    new_tags["tense"] = "<past><zhedel-otken>"
    new_tags["person"] = "<p2>"
    new_tags["plurality"] = "<pl>"
    result.append((tmp_new_word, new_tags))

    # 2 лицо (вежливое) ед.число
    tmp_new_word = add_affix_choosing_hard_or_soft(new_word,
                                                   hard_affix='ңыз',
                                                   soft_affix='ңіз')
    new_tags = tags.copy()
    new_tags["tense"] = "<past><zhedel-otken>"
    new_tags["person"] = "<p2_2>"
    new_tags["plurality"] = "<sg>"
    result.append((tmp_new_word, new_tags))

    # 2 лицо (вежливое) мн.число
    tmp_new_word = add_affix_choosing_hard_or_soft(new_word,
                                                   hard_affix='ңыздар',
                                                   soft_affix='ңіздер')
    new_tags = tags.copy()
    new_tags["tense"] = "<past><zhedel-otken>"
    new_tags["person"] = "<p2_2>"
    new_tags["plurality"] = "<pl>"
    result.append((tmp_new_word, new_tags))

    return result


def generate_all_buryngy_otken_shaq_1(word_and_tags: tuple) -> list:
    """функция, генерирующая бұрынғы өткен шақ 1 во всех лицах
    Основа глагола + -ған/-ген/-қан/-кен + личные окончания
    глухие -қан/-кен
    неглухие -ған/-ген
    """
    word, tags = word_and_tags
    result = []

    if word[-1] in voiceless_consonant:
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="қан",
                                                   soft_affix="кен")
    else:
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ған",
                                                   soft_affix="ген")
    new_tags = tags.copy()
    new_tags["tense"] = "<past><buryngy-otken-1>"

    # Добавляем все личные окончания
    result += generate_all_personals((new_word, new_tags))

    return result
