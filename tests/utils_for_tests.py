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
