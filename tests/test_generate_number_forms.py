from utils_for_tests import generate_results_to_test
from generate_number_forms import generate_ordinal_numeral
from generate_number_forms import generate_collective_numeral


def test_generate_ordinal_numeral():
    words_to_test = [("бір", dict()),
                     ("екі", dict()),
                     ("алты", dict()),
                     ("тоғыз", dict())]
    expected_results = ["бірінші",
                        "екінші",
                        "алтыншы",
                        "тоғызыншы"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_ordinal_numeral,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_collective_numeral():
    words_to_test = [("бір", dict()),
                     ("екі", dict()),
                     ("үш", dict()),
                     ("төрт", dict()),
                     ("бес", dict()),
                     ("алты", dict()),
                     ("жеті", dict())]
    expected_results = ["біреу",
                        "екеу",
                        "үшеу",
                        "төртеу",
                        "бесеу",
                        "алтау",
                        "жетеу"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_collective_numeral,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results
