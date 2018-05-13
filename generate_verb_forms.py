from morph_rules import vowels
from morph_rules import voiced_consonants
from morph_rules import voiceless_consonant
from morph_rules import add_affix_with_harmony
from morph_rules import add_affix_choosing_hard_or_soft
from common_forms import generate_all_long_personals_without_3p
from common_forms import generate_all_long_personals_with_3p
from common_forms import generate_all_short_personals


def generate_verb_forms(word_and_tags: tuple) -> list:
    """функция, генерирующая все формы для глагола
    """
    result = []
    result += generate_negative_verb(word_and_tags)
    result += generate_all_zhedel_otken_shaq(word_and_tags)
    result += generate_all_buryngy_otken_shaq_1(word_and_tags)
    result += generate_all_buryngy_otken_shaq_3(word_and_tags)
    result += generate_all_naq_osy_shaq(word_and_tags)
    # TODO добавить комбинации с отрицанием
    # (После основы вставляется аффикс отрицания)
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

    # добавляются -ды/-дi/-ты/-тi
    if word[-1] in voiceless_consonant:
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ты",
                                                   soft_affix="ті")
    else:
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ды",
                                                   soft_affix="ді")
    new_tags = tags.copy()
    new_tags["tense"] = "<past><zhedel-otken>"

    # добавляются краткие личные окончания
    result += generate_all_short_personals((new_word, new_tags))

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
    result += generate_all_long_personals_without_3p((new_word, new_tags))

    return result


def generate_all_buryngy_otken_shaq_3(word_and_tags: tuple) -> list:
    """функция, генерирующая бұрынғы өткен шақ 3 во всех лицах
    Основа глагола + -п/-ып/-іп + личные окончания
    гласные -п
    согласные -ып/-іп
    """
    word, tags = word_and_tags
    result = []

    if word[-1] in vowels:
        new_word = add_affix_with_harmony(word, affix='п')
    else:
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ып",
                                                   soft_affix="іп")
    new_tags = tags.copy()
    new_tags["tense"] = "<past><buryngy-otken-3>"

    # Добавляем все личные окончания
    result += generate_all_long_personals_with_3p((new_word, new_tags))

    return result


def generate_all_naq_osy_shaq(word_and_tags: tuple) -> list:
    """функция, генерирующая нақ осы шақ во всех лицах.
    Для 4 слов (тұр, отыр, жүр, жатыр)
    Основа глагола + личные окончания
    """
    word, tags = word_and_tags
    result = []

    if word in ("тұр", "отыр", "жүр", "жатыр"):
        new_tags = tags.copy()
        new_tags["tense"] = "<pres><naq-osy>"

        # Добавляем все личные окончания
        result += generate_all_long_personals_without_3p((word, new_tags))

    return result


def generate_all_auyspaly_osy_keler_shaq(word_and_tags: tuple) -> list:
    """функция, генерирующая ауыспалы осы/келер шақ во всех лицах.
    Основа глагола + -а/-е/-й + личные окончания (длинные с 3 лицом)
    а – в твёрдых словах
    е – в мягких словах
    й – после гласных
    """
    word, tags = word_and_tags
    result = []

    if word[-1] in vowels:
        new_word = add_affix_with_harmony(word, affix='й')
    else:
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix='а',
                                                   soft_affix='е')
    new_tags = tags.copy()
    new_tags["tense"] = "<pres><future>"

    # Добавляем все личные окончания
    result += generate_all_long_personals_with_3p((new_word, new_tags))

    return result


def generate_all_bolzhaldy_keler_shaq(word_and_tags: tuple) -> list:
    """функция, генерирующая болжалды келер шақ во всех лицах.
    Основа глагола + -ар/-ер/-р + личные окончания (длинные без 3 лица)
    ар – в твёрдых словах
    ер – в мягких словах
    р – после гласных
    """
    word, tags = word_and_tags
    result = []

    if word[-1] in vowels:
        new_word = add_affix_with_harmony(word, affix='р')
    else:
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix='ар',
                                                   soft_affix='ер')
    new_tags = tags.copy()
    new_tags["tense"] = "<future><bolzhaldy-keler>"

    # Добавляем все личные окончания
    result += generate_all_long_personals_without_3p((new_word, new_tags))

    return result
