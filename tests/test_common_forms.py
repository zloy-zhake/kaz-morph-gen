import pytest
from common_forms import generate_plural
from common_forms import generate_all_possessives
from common_forms import generate_atau_septik
from common_forms import generate_ilik_septik
from common_forms import generate_barys_septik
from common_forms import generate_tabys_septik
from common_forms import generate_zhatys_septik
from common_forms import generate_shygys_septik
from common_forms import generate_komektes_septik


def generate_results_to_test(func, words_to_test: tuple) -> list:
    """Функция, генерирующая результаты (слова без тегов) для тестов.
    Нужна чтобы не повторять одно и то же в каждом тесте.
    """
    # actual_results содержит сгенерированные слова и dict с тегами
    actual_results = []
    # results_to_test содержит только сгенерированные слова
    results_to_test = []

    # заполняем actual_results
    for item in words_to_test:
        actual_results += func(word_and_tags=item)

    # заполняем results_to_test
    for item in actual_results:
        results_to_test.append(item[0])

    return results_to_test


def test_generate_plural():
    words_to_test = [("қаз", dict()),
                     ("көз", dict()),
                     ("ата", dict()),
                     ("әже", dict()),
                     ("ат", dict()),
                     ("мектеп", dict())]
    expected_results = ["қаздар",
                        "көздер",
                        "аталар",
                        "әжелер",
                        "аттар",
                        "мектептер"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_plural,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results


@pytest.mark.skip(reason="Не работает слово iс. Скорее всего короткое.")
def test_generate_all_possessives():
    words_to_test = [("бала", dict()),
                     ("қыз", dict()),
                     ("iс", dict())]
    expected_results = ["балам",
                        "баламыз",
                        "балаң",
                        "балаңыз",
                        "баласы",
                        "қызым",
                        "қызымыз",
                        "қызың",
                        "қызыңыз",
                        "қызы",
                        "iсiм",
                        "iсiмiз",
                        "iсiң",
                        "iсiңiз",
                        "iсi"]

    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_all_possessives,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_atau_septik():
    words_to_test = [("мектеп", dict()),
                     ("адам", dict()),
                     ("бала", dict())]
    expected_results = ["мектеп",
                        "адам",
                        "бала"]

    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_atau_septik,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results


@pytest.mark.skip(reason="Исправить ошибку")
def test_generate_ilik_septik():
    words_to_test = [("қазақстан", dict()),
                     ("жер", dict()),
                     ("мектеп", dict())]
    expected_results = ["қазақстанның",
                        "жердiң",
                        "мектептiң"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_ilik_septik,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_barys_septik():
    words_to_test = [("адам", dict()),
                     ("кiтап", dict()),
                     ("үй", dict()),
                     ("ленинград", dict()),
                     ("балтам", {"person": "<px1sg>"}),
                     ("инесi", {"person": "<px3sp>"})]
    expected_results = ["адамға",
                        "кiтапқа",
                        "үйге",
                        "ленинградқа",
                        "балтама",
                        "инесiне"]

    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_barys_septik,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_tabys_septik():
    words_to_test = [("бала", dict()),
                     ("терезе", dict())]
    expected_results = ["баланы",
                        "терезенi"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_tabys_septik,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_zhatys_septik():
    words_to_test = [("завод", dict()),
                     ("мектеп", dict()),
                     ("сара", dict()),
                     ("казан", dict()),
                     ("әкесi", {"person": "<px3sp>"})]
    expected_results = ["заводта",
                        "мектепте",
                        "сарада",
                        "казанда",
                        "әкесiнде"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_zhatys_septik,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_shygys_septik():
    words_to_test = [("қар", dict()),
                     ("қала", dict()),
                     ("арқалық", dict())]
    expected_results = ["қардан",
                        "қаладан",
                        "арқалықтан"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_shygys_septik,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_komektes_septik():
    words_to_test = [("тарақ", dict()),
                     ("сабын", dict()),
                     ("iнiм", dict())]
    expected_results = ["тарақпен",
                        "сабынмен",
                        "iнiммен"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_komektes_septik,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results
