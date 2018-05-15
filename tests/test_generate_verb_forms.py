import pytest
from utils_for_tests import generate_results_to_test
from generate_verb_forms import generate_negative_verb
from generate_verb_forms import generate_all_zhedel_otken_shaq
from generate_verb_forms import generate_all_buryngy_otken_shaq_1
from generate_verb_forms import generate_all_buryngy_otken_shaq_3
from generate_verb_forms import generate_all_naq_osy_shaq
from generate_verb_forms import generate_all_auyspaly_osy_keler_shaq
from generate_verb_forms import generate_all_bolzhaldy_keler_shaq
from generate_verb_forms import generate_all_maqsatty_keler_shaq
from generate_verb_forms import generate_all_negative_maqsatty_keler_shaq
from generate_verb_forms import generate_all_imperative_mood
from generate_verb_forms import generate_all_conditional_mood
from generate_verb_forms import generate_reflexive_verb
from generate_verb_forms import generate_infinitive


def test_generate_negative_verb():
    words_to_test = [("сөйле", dict()),
                     ("іш", dict()),
                     ("тарт", dict())]
    expected_results = ["сөйлеме",
                        "ішпе",
                        "тартпа"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_negative_verb,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_all_zhedel_otken_shaq():
    words_to_test = [("жаз", dict())]
    expected_results = ["жаздым",
                        "жаздың",
                        "жаздыңыз",
                        "жаздық",
                        "жаздыңдар",
                        "жаздыңыздар",
                        "жазды"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = \
        generate_results_to_test(func=generate_all_zhedel_otken_shaq,
                                 words_to_test=words_to_test)
    assert results_to_test == expected_results


@pytest.mark.skip(reason="Исправить ошибку?")
def test_generate_all_buryngy_otken_shaq_1():
    words_to_test = [("асыра", dict())]
    expected_results = ["асырағанмын",
                        "асырағансың",
                        "асырағансыз",
                        "асырағанбыз",
                        "асырағансыңдар",
                        "асырағансыздар",
                        "асыраған"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = \
        generate_results_to_test(func=generate_all_buryngy_otken_shaq_1,
                                 words_to_test=words_to_test)
    assert results_to_test == expected_results


@pytest.mark.skip(reason="Исправить ошибку")
def test_generate_all_buryngy_otken_shaq_3():
    words_to_test = [("ұмыт", dict())]
    expected_results = ["ұмытыппын",
                        "ұмытыпсың",
                        "ұмытыпсыз",
                        "ұмытыппыз",
                        "ұмытыпсыңдар",
                        "ұмытыпсыздар",
                        "ұмытыпты"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = \
        generate_results_to_test(func=generate_all_buryngy_otken_shaq_3,
                                 words_to_test=words_to_test)
    assert results_to_test == expected_results


# TODO скорее всего, тут будет к месту параметризованный тест
def test_generate_all_naq_osy_shaq():
    words_to_test = [("тұр", dict()),
                     ("жүр", dict())]
    expected_results = ["тұрмын",
                        "тұрсың",
                        "тұрсыз",
                        "тұрмыз",
                        "тұрсыңдар",
                        "тұрсыздар",
                        "тұр",
                        "жүрмін",
                        "жүрсің",
                        "жүрсіз",
                        "жүрміз",
                        "жүрсіңдер",
                        "жүрсіздер",
                        "жүр"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = \
        generate_results_to_test(func=generate_all_naq_osy_shaq,
                                 words_to_test=words_to_test)
    assert results_to_test == expected_results


@pytest.mark.skip(reason="Ошибка в личных окончаниях. \
                          Проверить по другой книге")
def test_generate_all_auyspaly_osy_keler_shaq():
    words_to_test = [("істе", dict())]
    expected_results = ["істеймін",
                        "істейсің",
                        "істейсіз",
                        "істейміз",
                        "істейсіңдер",
                        "істейсіздер",
                        "істейді"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = \
        generate_results_to_test(func=generate_all_auyspaly_osy_keler_shaq,
                                 words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_all_bolzhaldy_keler_shaq():
    words_to_test = [("жаз", dict())]
    expected_results = ["жазармын",
                        "жазарсың",
                        "жазарсыз",
                        "жазармыз",
                        "жазарсыңдар",
                        "жазарсыздар",
                        "жазар"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = \
        generate_results_to_test(func=generate_all_bolzhaldy_keler_shaq,
                                 words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_all_maqsatty_keler_shaq():
    words_to_test = [("бар", dict())]
    expected_results = ["бармақпын",
                        "бармақсың",
                        "бармақсыз",
                        "бармақпыз",
                        "бармақсыңдар",
                        "бармақсыздар",
                        "бармақ"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = \
        generate_results_to_test(func=generate_all_maqsatty_keler_shaq,
                                 words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_all_negative_maqsatty_keler_shaq():
    words_to_test = [("бар", dict())]
    expected_results = ["бармаспын",
                        "бармассың",
                        "бармассыз",
                        "бармаспыз",
                        "бармассыңдар",
                        "бармассыздар",
                        "бармас"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = \
        generate_results_to_test(func=generate_all_negative_maqsatty_keler_shaq,
                                 words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_all_imperative_mood():
    words_to_test = [("ал", dict())]
    expected_results = ["алайын",
                        "ал",
                        "алыңыз",
                        "алайық",
                        "алыңдар",
                        "алыңыздар",
                        "алсын"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = \
        generate_results_to_test(func=generate_all_imperative_mood,
                                 words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_all_conditional_mood():
    words_to_test = [("бар", dict())]
    expected_results = ["барсам",
                        "барсаң",
                        "барсаңыз",
                        "барсақ",
                        "барсаңдар",
                        "барсаңыздар",
                        "барса"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = \
        generate_results_to_test(func=generate_all_conditional_mood,
                                 words_to_test=words_to_test)
    assert results_to_test == expected_results


@pytest.mark.skip(reason="Не работает слово. Скорее всего короткое.")
def test_generate_reflexive_verb():
    words_to_test = [("жу", dict())]
    expected_results = ["жуын"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_reflexive_verb,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results


def test_generate_infinitive():
    words_to_test = [("бар", dict())]
    expected_results = ["бару"]
    # results_to_test содержит только сгенерированные слова
    results_to_test = []
    results_to_test = generate_results_to_test(func=generate_infinitive,
                                               words_to_test=words_to_test)
    assert results_to_test == expected_results
