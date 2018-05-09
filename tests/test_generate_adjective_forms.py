from utils_for_tests import generate_results_to_test
from generate_adjective_forms import generate_comparative_adjective
from generate_adjective_forms import generate_superlative_adjective


def test_generate_comparative_adjective():
    words_to_test = [("жақсы", dict())]
    expected_results = ["жақсырақ",
                        "жақсылау"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = \
        generate_results_to_test(func=generate_comparative_adjective,
                                 words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_superlative_adjective():
    words_to_test = [("ақ", dict()),
                     ("көк", dict()),
                     ("жақсы", dict())]
    expected_results = ["аппақ",
                        "көкпенбек",
                        "жап-жақсы"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = \
        generate_results_to_test(func=generate_superlative_adjective,
                                 words_to_test=words_to_test)
    assert results_to_test == expected_results
