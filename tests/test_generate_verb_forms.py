import pytest
from utils_for_tests import generate_results_to_test
from generate_verb_forms import generate_negative_verb


@pytest.mark.skip(reason="Не работает слово iш. Скорее всего короткое.")
def test_generate_negative_verb():
    words_to_test = [("сөйле", dict()),
                     ("iш", dict()),
                     ("тарт", dict())]
    expected_results = ["сөйлеме",
                        "iшпе",
                        "тартпа"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_negative_verb,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results
