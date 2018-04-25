from morph_rules import vowels
from morph_rules import voiceless_consonant
from morph_rules import sonorous_consonants
from morph_rules import consonants
from morph_rules import add_affix_with_harmony
from morph_rules import add_affix_choosing_hard_or_soft


def generate_plural(word_and_tags: tuple) -> list:
    # region
    """Функция, генерирующая множественное число (көптiк).\n
    если слово заканчивается на ГЛАСНЫЙ, Р, Й, У
        - лар, - лер,
    если слово заканчивается на М, Н, Ң, Л, З
        - дар, - дер,
    если слово оканчивается на глухой согласный или Б, В, Г, Д
        - тар, - тер
    """
    # endregion

    word, tags = word_and_tags

    if (word[-1] in vowels) \
            or (word[-1] in ('р', 'й', 'у')):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="лар",
                                                   soft_affix="лер")

    elif word[-1] in ('м', 'н', 'ң', 'л', 'з'):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="дар",
                                                   soft_affix="дер")

    elif (word[-1] in voiceless_consonant) \
            or (word[-1] in ('б', 'в', 'г', 'д')):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="тар",
                                                   soft_affix="тер")

    new_tags = tags.copy()
    new_tags["plurality"] = "<pl>"

    # это странно, но по-другому один кортеж не возвращается ((
    result = []
    result.append((new_word, new_tags))
    return result


def generate_all_possessives(word_and_tags: tuple) -> list:
    # region
    """Функция, генерирующая притяжательную форму (тәуiлдiк).
    1 лицо ед.числа
    После гласных
        -м
    После согласных
        -ым, -iм

    1 лицо мн.числа
    После гласных
        -мыз, -мiз
    После согласных
        -ымыз, -iмiз

    2 лицо ед. и мн.числа
    После гласных
        -ң
    После согласных
        -ың, -iң

    2 лицо ед. и мн.числа (вежливое)
    После гласных
        -ңыз, -ңыз
    После согласных
        -ыңыз, -iңiз

    3 лицо ед. и мн. числа
    После гласных
        -сы, -сi
    После согласных
        -ы, -i
    """
    # endregion

    word, tags = word_and_tags
    result = []

    # 1 лицо ед.числа
    # После гласных
    #     -м
    # После согласных
    #     -ым, -iм

    if (word[-1] in vowels):
        new_word = add_affix_with_harmony(word, affix='м')
    elif (word[-1] in consonants):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ым",
                                                   soft_affix="ім")
    new_tags = tags.copy()
    new_tags["person"] = "<p1>"
    new_tags["possession"] = "<px1sg>"
    result.append((new_word, new_tags))

    # 1 лицо мн.числа
    # После гласных
    #     -мыз, -мiз
    # После согласных
    #     -ымыз, -iмiз
    if (word[-1] in vowels):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="мыз",
                                                   soft_affix="мiз")
    elif (word[-1] in consonants):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ымыз",
                                                   soft_affix="iмiз")
    new_tags = tags.copy()
    new_tags["person"] = "<p1>"
    new_tags["possession"] = "<px1pl>"
    result.append((new_word, new_tags))

    # 2 лицо ед. и мн.числа
    # После гласных
    #     -ң
    # После согласных
    #     -ың, -iң
    if (word[-1] in vowels):
        new_word = add_affix_with_harmony(word, affix='ң')
    elif (word[-1] in consonants):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ың",
                                                   soft_affix="iң")
    # тут подходят px2sg и px2pl, пока ставится "объединенный вариант"
    new_tags = tags.copy()
    new_tags["person"] = "<p2>"
    new_tags["possession"] = "<px2sp>"
    result.append((new_word, new_tags))

    # 2 лицо ед. и мн.числа (вежливое)
    # После гласных
    #     -ңыз, -ңiз
    # После согласных
    #     -ыңыз, -iңiз
    if (word[-1] in vowels):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ңыз",
                                                   soft_affix="ңiз")
    elif (word[-1] in consonants):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ыңыз",
                                                   soft_affix="iңiз")
    # тут подходят px2sg и px2pl, пока ставится "объединенный вариант"
    # TODO придумать тег для вежлифой формы
    new_tags = tags.copy()
    new_tags["person"] = "<p2_2>"
    new_tags["possession"] = "<px2sp_2>"
    result.append((new_word, new_tags))

    # 3 лицо ед. и мн. числа
    # После гласных
    #     -сы, -сi
    # После согласных
    #     -ы, -i
    if (word[-1] in vowels):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="сы",
                                                   soft_affix="сi")
    elif (word[-1] in consonants):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ы",
                                                   soft_affix="i")
    new_tags = tags.copy()
    new_tags["person"] = "<p3>"
    new_tags["possession"] = "<px3sp>"
    result.append((new_word, new_tags))

    return result


def generate_all_cases(word_and_tags: tuple) -> list:
    """Функция, генерирующая все падежи, вызывая генератор каждого.
    """
    result = []

    result += generate_atau_septik(word_and_tags)
    result += generate_ilik_septik(word_and_tags)
    result += generate_barys_septik(word_and_tags)
    result += generate_tabys_septik(word_and_tags)
    result += generate_zhatys_septik(word_and_tags)
    result += generate_shygys_septik(word_and_tags)
    result += generate_komektes_septik(word_and_tags)

    return result


def generate_atau_septik(word_and_tags: tuple) -> list:
    """Функция, генерирующая атау септік (nominative case).
    """
    word, tags = word_and_tags
    new_tags = tags.copy()
    new_tags["case"] = "<nom>"
    result = []
    result.append((word, new_tags))
    return result


def generate_ilik_septik(word_and_tags: tuple) -> list:
    """Функция, генерирующая ілік септік (genitive case).
    Гласные + м, н, ң
        -ның, -нiң
    ж, з, р, л, и, у
        -дың, -дiң
    Глухие + б, в, с, д
        -тың, -тiң
    """
    word, tags = word_and_tags
    result = []

    if (word[-1] in vowels) \
            or (word[-1] in ['м', 'н', 'ң']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ның",
                                                   soft_affix="нiң")
    elif word[-1] in ['ж', 'з', 'р', 'л', 'и', 'у']:
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="дың",
                                                   soft_affix="дiң")
    elif (word[-1] in voiceless_consonant) \
            or (word[-1] in ['б', 'в', 'с', 'д']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="тiң",
                                                   soft_affix="тың")
    new_tags = tags.copy()
    new_tags["case"] = "<gen>"
    result.append((new_word, new_tags))

    return result


def generate_barys_septik(word_and_tags: tuple) -> list:
    """Функция, генерирующая барыс септік (dative case).
    После принадлежности аффиксов 1 и 2 лица
        -а, -е
    После принадлежности аффиксов 3-го лица
        -на, -не
    Гласные, сонорные и ж, з
        -ға, -ге
    Глухие и б, в, г, д
        -қа, -ке
    """
    word, tags = word_and_tags
    result = []

    if "<px1sg>" in tags.values() \
            or "<px2sp>" in tags.values():
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix='а',
                                                   soft_affix='е')
    elif "<px3sp>" in tags.values():
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="на",
                                                   soft_affix="не")
    elif (word[-1] in vowels) \
            or (word[-1] in sonorous_consonants) \
            or (word[-1] in ['ж', 'з']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ға",
                                                   soft_affix="ге")
    elif (word[-1] in voiceless_consonant) \
            or (word[-1] in ['б', 'в', 'г', 'д']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="қа",
                                                   soft_affix="ке")
    new_tags = tags.copy()
    new_tags["case"] = "<dat>"
    result.append((new_word, new_tags))

    return result


def generate_tabys_septik(word_and_tags: tuple) -> list:
    """Функция, генерирующая табыс септік (accusative case).
    После аффиксов 3-го лица
        -н
    Гласные
        -ны, -нi
    Сонорные и з, ж
        -ды, -дi
    Глухие и б, в, г, д
        -ты, -тi
    """
    word, tags = word_and_tags
    result = []

    if "<px3sp>" in tags.values():
        new_word = add_affix_with_harmony(word, affix='н')
    elif (word[-1] in vowels):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ны",
                                                   soft_affix="нi")
    elif (word[-1] in sonorous_consonants) \
            or (word[-1] in ['з', 'ж']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ды",
                                                   soft_affix="дi")
    elif (word[-1] in voiceless_consonant) \
            or (word[-1] in ['б', 'в', 'г', 'д']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ты",
                                                   soft_affix="тi")
    new_tags = tags.copy()
    new_tags["case"] = "<acc>"
    result.append((new_word, new_tags))

    return result


def generate_zhatys_septik(word_and_tags: tuple) -> list:
    """Функция, генерирующая жатыс септік (locative case).
    После аффиксов 3-го лица
        -нда, -нде
    Гласные, сонорные и ж, з
        -да, -де
    Глухие и б, в, г, д
        -та, -те
    """
    word, tags = word_and_tags
    result = []

    if "<px3sp>" in tags.values():
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="нда",
                                                   soft_affix="нде")
    elif (word[-1] in vowels) \
            or (word[-1] in sonorous_consonants) \
            or (word[-1] in ['ж', 'з']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="да",
                                                   soft_affix="де")
    elif (word[-1] in voiceless_consonant) \
            or (word[-1] in ['б', 'в', 'г', 'д']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="та",
                                                   soft_affix="те")
    new_tags = tags.copy()
    new_tags["case"] = "<loc>"
    result.append((new_word, new_tags))

    return result


def generate_shygys_septik(word_and_tags: tuple) -> list:
    """Функция, генерирующая шығыс септік (ablative case).
    Гласные и з, ж, р, й, л, у
        -дан, -ден
    м, н, ң
        -нан, -нен
    Глухие и б, в, г, д
        -тан, -тен
    """
    word, tags = word_and_tags
    result = []

    if (word[-1] in vowels) \
            or (word[-1] in ['з', 'ж', 'р', 'й', 'л', 'у']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="дан",
                                                   soft_affix="ден")
    elif (word[-1] in ['м', 'н', 'ң']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="нан",
                                                   soft_affix="нен")
    elif (word[-1] in voiceless_consonant) \
            or (word[-1] in ['б', 'в', 'г', 'д']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="тан",
                                                   soft_affix="тен")
    new_tags = tags.copy()
    new_tags["case"] = "<abl>"
    result.append((new_word, new_tags))

    return result


def generate_komektes_septik(word_and_tags: tuple) -> list:
    """Функция, генерирующая көмектес септік (instrumental case).
    Гласные и м, н, ң, р, л
        -мен
    ж, з
        -бен
    Глухие и б, в, г, д
        -пен
    """
    word, tags = word_and_tags
    result = []

    if (word[-1] in vowels) \
            or (word[-1] in ['м', 'н', 'ң', 'р', 'л']):
        new_word = add_affix_with_harmony(word, affix="мен")
    elif (word[-1] in ['ж', 'з']):
        new_word = add_affix_with_harmony(word, affix="бен")
    elif (word[-1] in voiceless_consonant) \
            or (word[-1] in ['б', 'в', 'г', 'д']):
        new_word = add_affix_with_harmony(word, affix="пен")

    new_tags = tags.copy()
    new_tags["case"] = "<ins>"
    result.append((new_word, new_tags))

    return result


def generate_all_personals(word_and_tags: tuple) -> list:
    # region
    """Функция, генерирующая личную форму (жіктік).
    1 лицо ед.числа
        -мын, -мін
        -бын, -бін
        -пын, -пін

    2 лицо ед.числа
        -сың, -сің

    2 лицо ед.числа (вежливое)
        -сыз, -сіз

    1 лицо мн.числа
        -мыз, -міз
        -быз, -біз
        -пыз, -піз

    2 лицо мн.числа
        -сыңдар, -сіңдер

    2 лицо мн.числа (вежливое)
        -сыздар, -сіздер

    3 лицо ед. и мн. числа
        -
    """
    # endregion

    word, tags = word_and_tags
    result = []

    # ед.число
    if ("plurality" not in tags) or (tags["plurality"] != "<pl>"):
        # 1 лицо ед.числа
        #     -мын, -мін
        #     -бын, -бін
        #     -пын, -пін
        if (word[-1] in vowels) \
                or (word[-1] in ['м', 'н', 'ң', 'р', 'л']):
            new_word = add_affix_choosing_hard_or_soft(word,
                                                       hard_affix="мын",
                                                       soft_affix="мін")
        elif (word[-1] in ['ж', 'з']):
            new_word = add_affix_choosing_hard_or_soft(word,
                                                       hard_affix="бын",
                                                       soft_affix="бін")
        elif (word[-1] in voiceless_consonant) \
                or (word[-1] in ['б', 'в', 'г', 'д']):
            new_word = add_affix_choosing_hard_or_soft(word,
                                                       hard_affix="пын",
                                                       soft_affix="пін")
        new_tags = tags.copy()
        new_tags["person"] = "<p1>"
        new_tags["plurality"] = "<sg>"
        result.append((new_word, new_tags))

        # 2 лицо ед.числа
        # -сың, -сің
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="сың",
                                                   soft_affix="сің")
        new_tags = tags.copy()
        new_tags["person"] = "<p2>"
        new_tags["plurality"] = "<sg>"
        result.append((new_word, new_tags))

        # 2 лицо ед.числа (вежливое)
        #     -сыз, -сіз
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="сыз",
                                                   soft_affix="сіз")
        new_tags = tags.copy()
        new_tags["person"] = "<p2_2>"
        new_tags["plurality"] = "<sg>"
        result.append((new_word, new_tags))

    # мн.число

    # 1 лицо мн.числа
    # -мыз, -міз
    # -быз, -біз
    # -пыз, -піз
    if (word[-1] in vowels) \
            or (word[-1] in ['м', 'н', 'ң', 'р', 'л']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="мыз",
                                                   soft_affix="міз")
    elif (word[-1] in ['ж', 'з']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="быз",
                                                   soft_affix="біз")
    elif (word[-1] in voiceless_consonant) \
            or (word[-1] in ['б', 'в', 'г', 'д']):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="пыз",
                                                   soft_affix="піз")
    new_tags = tags.copy()
    new_tags["person"] = "<p1>"
    new_tags["plurality"] = "<pl>"
    result.append((new_word, new_tags))

    # 2 лицо мн.числа
    # -сыңдар, -сіңдер
    new_word = add_affix_choosing_hard_or_soft(word,
                                               hard_affix="сыңдар",
                                               soft_affix="сіңдер")
    new_tags = tags.copy()
    new_tags["person"] = "<p2>"
    new_tags["plurality"] = "<pl>"
    result.append((new_word, new_tags))

    # 2 лицо мн.числа (вежливое)
    # -сыздар, -сіздер
    new_word = add_affix_choosing_hard_or_soft(word,
                                               hard_affix="сыздар",
                                               soft_affix="сіздер")
    new_tags = tags.copy()
    new_tags["person"] = "<p2_2>"
    new_tags["plurality"] = "<pl>"
    result.append((new_word, new_tags))

    return result
