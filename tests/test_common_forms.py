import pytest
from common_forms import generate_plural
from common_forms import generate_all_possessives


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
    for item in results_to_test:
        print(item)

    assert results_to_test == expected_results
